let line = [2, 1, -1, -2, -2, -1, 1, 2];
let column = [1, 2, 2, 1, -1, -2, -2, -1];
let sizeboard = 8;

let lin = 0;
let col = 0;

let board = new Array(sizeboard);
for (let i = 0; i < sizeboard; i++) {
    board[i] = new Array(sizeboard);
}
for (let i = 0; i < sizeboard; i++) {
    for (let j = 0; j < sizeboard; j++)
        board[i][j] = 0
}

let limit = sizeboard * sizeboard



function main(l, c){
    board [l][c] = 1;

    movehorse(2, l, c)
}

function movehorse(id, l, c){
    if (id > limit){
        console.log("solução encontrada")
        console.table(board)
       
    }
        
    let k 


    for ( k = 0; k < 8; k++){
        let x = l + line[k]
        let y = c + column[k]

        if (movacceptable(x, y) == true){
            board[x][y] = id
            movehorse(id + 1, x, y)
            board[x][y] = 0
        }
    }
        
}

function movacceptable(x, y) {
    if ((x >= 0 && x < sizeboard) && (y >= 0 && y < sizeboard) && (board[x][y] == 0)) {
        return true
    }
    else {
        return false
    }
}


main(lin, col)