document.addEventListener('DOMContentLoaded', () => {
    document.getElementById("pizza_link").onclick = () => showMenuItem("pizza_menu");
    document.getElementById("subs_link").onclick = () => showMenuItem("subs_menu");
    document.getElementById("salads_link").onclick = () => showMenuItem("salads_menu");
    document.getElementById("pasta_link").onclick = () => showMenuItem("pasta_menu");
    document.getElementById("platers_link").onclick = () => showMenuItem("platers_menu");

    showMenuItem("pizza_menu")
});

function showMenuItem(toShow){
    document.getElementById("menu_container").querySelectorAll('*').forEach(menu=>menu.style.display = 'none');
    document.getElementById(toShow).style.display = "block";
    return false;
};
