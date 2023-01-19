var r = document.querySelector(':root');
r.style.setProperty('--theme', 'dark');

function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

const getCookie = (name) => (
    document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''
)

var cookieAccepted = getCookie("cookie")
if (cookieAccepted == "true") {
    document.getElementsByClassName('cookieadvise').item(0).style.display = 'none';
}

var cookieTheme = getCookie("theme");
if (cookieTheme == "dark") {
    r.style.setProperty('--theme', 'dark');
    darkTheme();
    document.getElementsByClassName("switch").item(0).children.item(0).checked = false;
} else if (cookieTheme == "light") {
    r.style.setProperty('--theme', 'light');
    lightTheme();
    document.getElementsByClassName("switch").item(0).children.item(0).checked = true;
} else {
    darkTheme();
    document.getElementsByClassName("switch").item(0).children.item(0).checked = false;
    setCookie("theme", "dark", 30);
}

function themeSwitch() {
    // get the current theme
    var currentTheme = window.getComputedStyle(document.documentElement).getPropertyValue('--theme');
    // if the current theme is dark, switch to light
    if (currentTheme == 'dark') {
        r.style.setProperty('--theme', 'light');
        setCookie("theme", "light", 30);
        lightTheme();
    }
    // if the current theme is light, switch to dark
    else {
        r.style.setProperty('--theme', 'dark');
        setCookie("theme", "dark", 30);
        darkTheme();
    }

}

function lightTheme() {
    r.style.setProperty('--1', '#d5d5d5ff');
    r.style.setProperty('--2', '#ffffffff');
    r.style.setProperty('--3', '#757575ff');
    r.style.setProperty('--4', '#b6b6b6ff');
    r.style.setProperty('--5', '#858585ff');
    r.style.setProperty('--6', '#b1b1b1ff');
    r.style.setProperty('--7', '#414141ff');
    r.style.setProperty('--8', '#2f2f2fff');
    r.style.setProperty('--9', '#111111ff');
    r.style.setProperty('--10', '#000000ff');
}
function darkTheme() {
    r.style.setProperty('--1', '#111111ff');
    r.style.setProperty('--2', '#161723ff');
    r.style.setProperty('--3', '#0d0c34ff');
    r.style.setProperty('--4', '#0f0c75ff');
    r.style.setProperty('--5', '#16144fff');
    r.style.setProperty('--6', '#29275aff');
    r.style.setProperty('--7', '#4e4d6fff');
    r.style.setProperty('--8', '#747384ff');
    r.style.setProperty('--9', '#999999ff');
    r.style.setProperty('--10', '#ffffffff');
}

// make the function rickroll
function rickroll() {
    window.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ');
}

function closeCookies() {
    document.getElementsByClassName('cookieadvise').item(0).style.display = 'none';
    setCookie("cookie", "true", 7)
}