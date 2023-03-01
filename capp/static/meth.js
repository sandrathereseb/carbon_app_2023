var voksen = document.getElementById("kek");
const drop1 = document.getElementById('one');
drop1.addEventListener('click', (e) => {
    dropin1()
})
function dropin1() {
    if (voksen.style.display === "none") {
        voksen.style.display = "block";
    } else {
        voksen.style.display = "none"
    }
}

var barn = document.getElementById("kektwo");
const drop2 = document.getElementById('two');
drop2.addEventListener('click', (e) => {
    dropin2()
})
function dropin2() {
    if (barn.style.display === "none") {
        barn.style.display = "block";
    } else {
        barn.style.display = "none"
    }
}