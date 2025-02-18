document.addEventListener("DOMContentLoaded", () => {
    const cells = document.querySelectorAll(".cell");
    const message = document.getElementById("message");

    cells.forEach(cell => {
        cell.addEventListener("click", () => {
            const position = cell.getAttribute("data-position");
            makeMove(position);
        });
    });
});

function makeMove(position) {
    fetch("/play", {
        method: "POST",
        body: JSON.stringify({ position: parseInt(position) }),
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        updateBoard(data.board);
        updateMessage(data.player, data.winner);
    });
}

function updateBoard(board) {
    for (let i = 1; i <= 9; i++) {
        let cell = document.getElementById("cell" + i);
        cell.textContent = board[i];
        if (board[i] !== " ") {
            cell.classList.add("taken");
        }
    }
}

function updateMessage(player, winner) {
    const message = document.getElementById("message");
    if (winner) {
        message.textContent = winner;
    } else {
        message.textContent = `Player ${player}'s turn`;
    }
}

function resetGame() {
    fetch("/reset", { method: "POST" })
    .then(response => response.json())
    .then(() => {
        location.reload();
    });
}
