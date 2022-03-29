//define array for the entry boxes, and get a matrix of the IDs
let box = [];

for (let i = 0; i < 5; i++) {
    box[i] = [];
    for (let j = 1; j <= 5; j++) {
        box[i][j] = { "component": "guess_input", "guess_number": j, "letter_position": i };
    }
}

//need to wait for the DOM to load (some weird react js behaviour means that window.onload doesn't work), so keep checking until last box is loaded.
function loadfunc() {
    if (document.getElementById(JSON.stringify(box[4][5])) == null) {
        window.requestAnimationFrame(loadfunc);
    } else {
        for (let i = 0; i < 4; i++) {
            for (let j = 1; j <= 5; j++) {
                document.getElementById(JSON.stringify(box[i][j])).addEventListener("keyup", function () { if (this.value.length > 0) { document.getElementById(JSON.stringify(box[i + 1][j])).focus() } });
            }
        }
        // add segment keystroke tracking
        for (let i = 0; i < 5; i++) {
            for (let j = 1; j <= 5; j++) {
                document.getElementById(JSON.stringify(box[i][j])).addEventListener("keyup", function (event) {
                    analytics.track('Keystroke', {
                        character: event.key,
                        position: i,
                        guess: j
                    });
                })
            }
        }
    }
};

loadfunc();