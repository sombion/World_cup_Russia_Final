let score = 0;

function checkWin() {
    const runningBar = document.getElementById('running-bar');
    const runningBarRect = runningBar.getBoundingClientRect();
    const greenZone = document.getElementById('green-zone');
    const greenZoneRect = greenZone.getBoundingClientRect();
    const result = document.getElementById('result');

    if (runningBarRect.left >= greenZoneRect.left && runningBarRect.right <= greenZoneRect.right) {
        
        fillScore();
    } else {
        
		nullScore();
    }
	if (score == 3) {
		result.textContent = 'Победа!';
        result.style.color = 'green';
	} 
	if (score == 0) {
		result.textContent = 'Поражение!';
        result.style.color = 'red';
	}
}

function fillScore() {
    if (score < 3) {
        score++;
        document.getElementById(`score-circle-${score}`).style.backgroundColor = 'green';
    }
}

function nullScore() {
	score = 0;
	document.getElementById(`score-circle-${1}`).style.backgroundColor = 'gray';
	document.getElementById(`score-circle-${2}`).style.backgroundColor = 'gray';
	document.getElementById(`score-circle-${3}`).style.backgroundColor = 'gray';

}

function setGreenZone(startPercent, widthPercent) {
    const greenZone = document.getElementById('green-zone');
    greenZone.style.left = `${startPercent}%`;
    greenZone.style.width = `${widthPercent}%`;
}

// Пример установки зелёной зоны на 60% начала и 20% ширины
setGreenZone(60, 20);
