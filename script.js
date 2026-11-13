function updateLeaderboard(length) {
    const leaderboardLength = length || 10;
    const table = document.getElementById("leaderboardDisplay");
    table.innerHTML = "";
    addHeader(table);
    for (let i = 1; i <= leaderboardLength; i++) {
        const row = document.createElement("tr");
        row.id = `row${i}`
        //GET API DATA
        row.innerHTML = `
            <th class="leaderboardPlace">#${i}</th>
            <th class="leaderboardUsername">${/* GET NAME */ null}</th>
            <th class="leaderboardScore">${/* GET NAME */ null}</th>
        `;
        table.appendChild(row);
    }
}

function addHeader(table) {
    const leaderboardHeader = document.createElement("tr");
    //leaderboardHeader.className = "milestone";
    leaderboardHeader.innerHTML = `
        <th>Score</th>
        <th>Name</th>
        <th>Score</th>
    `;
    table.appendChild(leaderboardHeader);

}