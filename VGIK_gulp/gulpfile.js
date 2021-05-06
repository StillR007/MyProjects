const del = require('del');
const fileinclude = require('gulp-file-include');

let project_folder = "dist";
let source_folder = "src";

let path={
    build: {
        html: project_folder+"/",
        css: project_folder + "/css/",
        js: project_folder + "/js/",
        img: project_folder + "/img/",
        fonts: project_folder + "/fonts/",
        video: project_folder + "/video/"
    },
    src: {
        html: [source_folder+"/*.html", "!" + source_folder + "/_*.html"],
        css: source_folder + "/scss/style.scss",
        js: source_folder + "/js/script.js",
        img: source_folder + "/img/**/*.{jpg,png,ico}",
        fonts: source_folder + "/fonts/*.{ttf,eot,svg,woff,woff2}",
        video: source_folder + "/video/*.{mp4,webm}"
    },
    watch: {
        html: source_folder+"/**/*.html",
        css: source_folder + "scss/**/*.scss",
        js: source_folder + "/js/**/*.js",
        img: source_folder + "/img/**/*.{jpg,png,ico}",
        fonts: source_folder + "/fonts/*.{ttf,eot,svg,woff,woff2}",
        video: source_folder + "/video/*.{mp4,webm}"
    },
    clean: "./" + project_folder + "/"
}

let {src, dest} = require('gulp'),
    gulp = require('gulp'),
    browsersync = require("browser-sync").create(),
    scss = require("gulp-sass"),
    autoprefixer = require("gulp-autoprefixer"),
    group_media = require("gulp-group-css-media-queries"),
    clean_css = require("gulp-clean-css"),
    rename = require("gulp-rename"),
    uglify = require("gulp-uglify-es").default,
    imagemin = require("gulp-imagemin"),
    webp = require("gulp-webp"),
    webphtml = require("gulp-webp-html");

function browserSync() {
    browsersync.init({
       server: {
           baseDir: "./" + project_folder + "/",
       },
       port: 3000,
    })
}

function html() {
    return src(path.src.html)
        .pipe(fileinclude())
        .pipe(webphtml())
        .pipe(dest(path.build.html))
        .pipe(browsersync.stream())
}

function css() {
    return src(path.src.css)
        .pipe(
            scss({
                outputStyle: "expanded"
            })
        )
        .pipe(
            group_media()
        )
        .pipe(
            autoprefixer({
                overrideBrowserslist: ["last 5 versions"],
                cascade: true
            })
        )
        .pipe(dest(path.build.css))
        .pipe(clean_css())
        .pipe(
            rename({
                extname: ".min.css"
            })
        )
        .pipe(dest(path.build.css))
        .pipe(browsersync.stream())
}

function fonts () {
    src(path.src.fonts)

        .pipe(dest(path.build.fonts))
    return src(path.src.fonts)
        .pipe(dest(path.build.fonts))
}

function images() {
    return src(path.src.img)
        .pipe(
            webp({
                quality: 100 // 0 to 100
            })
        )
        .pipe(dest(path.build.img))
        .pipe(src(path.src.img))
        .pipe(
            imagemin({
                progressive: true,
                svgoPlugins: [{ removeViewBox: false}],
                interlaced: true,
                optimizationLevel: 0 // 0 to 7
            })
        )
        .pipe(dest(path.build.img))
        .pipe(browsersync.stream())
}

function js() {
    return src(path.src.js)
        .pipe(fileinclude())
        .pipe(dest(path.build.js))
        .pipe(
            uglify()
        )
        .pipe(
            rename({
                extname: ".min.js"
            })
        )
        .pipe(dest(path.build.js))
        .pipe(browsersync.stream())
}

function video () {
    return src(path.src.video)
        .pipe(fileinclude())
        .pipe(dest(path.build.video))
}


function watchFiles (params) {
    gulp.watch([path.watch.html], html),
    gulp.watch([path.watch.css], css),
    gulp.watch([path.watch.js], js),
    gulp.watch([path.watch.img], images),
    gulp.watch([path.watch.video], video)
}


function clean (params) {
    return del(path.clean);
}

let build = gulp.series(clean, gulp.parallel(js, css, html, images, fonts, video));
let watch = gulp.parallel(build, watchFiles, browserSync);

exports.video = video;
exports.fonts = fonts;
exports.images = images;
exports.js = js;
exports.css = css;
exports.html = html;
exports.build = build;
exports.watch = watch;
exports.default = watch;