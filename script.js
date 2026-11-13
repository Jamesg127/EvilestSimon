function loadLeaderboard() {
    const table = document.getElementById("leaderboardDisplay");
    table.innerHTML = "";
    const leaderboardHeader = document.createElement("tr");
    //leaderboardHeader.className = "milestone";
    leaderboardHeader.innerHTML = `
        <th>Score</th>
        <th>Name</th>
        <th>Score</th>
    `;
    table.appendChild(leaderboardHeader);
}