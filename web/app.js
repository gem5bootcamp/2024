/* Constant parameters */
const slide_url_base = './slides/'
const slide_url_ext = '.html'
const slide_link_height = 25;

/* Global references and variables */
let slide_list = [];
let slide_id = -1;

window.addEventListener('load', function() {
    let slide_registry = get_slide_registry();
    populate_sidebar(slide_registry);

    /* Follow url hash */
    document.querySelector('#slideFrame').addEventListener('load', slide_onload);
    route(window.location.hash, false);
});

/* ========================================================================= *
 * Routing
 * ========================================================================= */

function route(url, push=true) {
    if (push) {
        /* Push onto browser history */
        window.history.pushState('', '', url);
    }
    /* Check for home page */
    let home = document.querySelector('#home');
    if (url === '' || url === '#') {
        home.classList.remove('hidden');
        return;
    }
    home.classList.add('hidden');
    /* Set iframe src */
    let full_url = slide_url_base + url.substring(1) + slide_url_ext;
    document.querySelector('#slideFrame').src = full_url;
    document.querySelector('#slideFrame').title = url;
    /* Find slide id number */
    slide_id = -1;
    for (const slide of slide_list) {
        if (url === slide.getAttribute('slide-url')) {
            slide_id = parseInt(slide.getAttribute('slide-id'));
            break;
        }
    }
    if (slide_id < 0) {
        /* Slide not found, just bring up splash page to hide the mess */
        home.classList.remove('hidden');
    } else {
        home.classList.add('hidden');
    }
    /* Configure buttons */
    let prev = document.querySelector('#prevSlide');
    let next = document.querySelector('#nextSlide');
    if (slide_id <= 0) {
        prev.classList.add('hidden');
    } else {
        prev.classList.remove('hidden');
        prev.children[1].textContent = slide_list[slide_id - 1].textContent;
    }
    if (slide_id >= slide_list.length - 1) {
        next.classList.add('hidden');
    } else {
        next.classList.remove('hidden');
        next.children[1].textContent = slide_list[slide_id + 1].textContent;
    }
}

window.addEventListener('popstate', () => {
	route(window.location.hash, false);
});

/* ========================================================================= *
 * Slide Navigation
 * ========================================================================= */

function prev_slide() {
    if (slide_id > 0) {
        route(slide_list[slide_id - 1].getAttribute('slide-url'));
    }
}

function next_slide() {
    if (slide_id < slide_list.length - 1) {
        route(slide_list[slide_id + 1].getAttribute('slide-url'));
    }
}

function sidebar_category_onclick(e) {
    let curr_clicked = this.parentElement;
    let prev_selected = document.querySelectorAll('.sidebar-category.selected');
    /* Close all previously selected categories */
    let clicked_already_selected = false;
    for (const cat of prev_selected) {
        cat.classList.remove('selected');
        cat.children[1].style.height = '';
        if (cat === curr_clicked)
            clicked_already_selected = true;
    }
    /* Clicking already-selected button should just close it */
    if (clicked_already_selected)
        return;
    /* Open category */
    let slides = curr_clicked.children[1];
    curr_clicked.classList.add('selected');
    let height = slide_link_height * slides.children.length;
    slides.style.height = `${height}px`;
}

/* ========================================================================= *
 * Slide Augmentation
 * ========================================================================= */

function slide_onload(event) {
    /* Have all hyperlinks in iframe open in new tab */
    let frame = document.querySelector('#slideFrame');
    let links = frame.contentDocument.querySelectorAll('a');
    for (const a of links) {
        a.setAttribute('target', '_blank');
    }
}

/* ========================================================================= *
 * Element generators and DOM populators
 * ========================================================================= */

function make_slide_link(name, link) {
    let elem = document.createElement('div');
    elem.classList.add('slide-link');
    elem.textContent = name;
    elem.href = '#';
    elem.setAttribute('slide-id', slide_list.length);
    elem.setAttribute('slide-url', link);
    elem.addEventListener('click', (e) => {
        e.preventDefault();
        route(elem.getAttribute('slide-url'));
    });
    slide_list.push(elem);
    return elem;
}

function make_category(cat) {
    let elem = document.createElement('div');
    elem.classList.add('sidebar-category');
    /* Add `category-button` */
    elem.append((() => {
        let elem = document.createElement('div');
        elem.classList.add('category-button');
        elem.onclick = sidebar_category_onclick;
        /* Add `category-name` */
        elem.append((() => {
            let elem = document.createElement('span');
            elem.classList.add('category-name');
            elem.textContent = cat.name;
            return elem;
        })());
        /* Add `dropdown-arrow` */
        elem.append((() => {
            let elem = document.createElement('span');
            elem.classList.add('dropdown-arrow');
            elem.textContent = '>';
            return elem;
        })());
        return elem;
    })());

    /* Add slide links */
    let link_base = `#${cat.name}/`;
    elem.append((() => {
        let elem = document.createElement('div');
        elem.classList.add('category-slides');
        for (const slide of cat.slides) {
            elem.append(make_slide_link(slide, `${link_base}${slide}`));
        }
        return elem;
    })());

    return elem;
}

function populate_sidebar(slide_registry) {
    let sidebar = document.querySelector('.sidebar');
    for (const cat of slide_registry) {
        sidebar.append(make_category(cat));
    }
}