// displays the stars
function newStar(){
    var star = document.createElement('span');
    star.classList.add('material-icons');
    star.textContent = 'star';
    return star
};

function newEmptyStar(){
    var star = document.createElement('span');
    star.classList.add('material-icons');
    star.textContent = 'star_outline';
    return star
};

function create_stars(elem, value){
    value = Number(value);
    empty = 5 - value;
    for (var i=0; i < value; i++){
        elem.appendChild(newStar());
    }
    for (var i=0; i < empty; i++){
        elem.appendChild(newEmptyStar());
    }
};

let ratings = document.getElementsByClassName('rating');
Array.from(ratings).forEach((rating) => {
    create_stars(rating, rating.getAttribute('rating'));
});
