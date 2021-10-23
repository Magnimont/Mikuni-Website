function fetchData() {
	fetch('https://api.statcord.com/v3/900959366646226974').then(response => {
		return response.json();
	}).then(data => {
		console.log(data.data[0].servers);
		document.querySelector('#server-count').innerHTML = `<p>${data.data[0].servers}+</p>`
		console.log(data.data[0].users);
		document.querySelector('#user-count').innerHTML = `<p>${data.data[0].users}+</p>`
	}).catch(error => {
		console.log(error);
	});
	fetch('https://api.statcord.com/v3/900959366646226974/aggregate').then(response => {
		return response.json();
	}).then(data => {
		document.querySelector('#cmd-count').innerHTML = `<p>${data.data.totalCommands}+</p>`
	}).catch(error => {
		console.log(error);
	})
}

fetchData();

// Amongus beetches

console.log("susu")
