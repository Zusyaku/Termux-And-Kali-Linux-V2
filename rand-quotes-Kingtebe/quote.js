/**
Author : Kingtebe
Date : April 23, 14:21 WIB 2021
**/

const request = require('request');

var blue = '\033[34m';
var white = '\033[37m';

function quotes(){
	const logo = (`\n\n	      Quotes Random\n          made by ${blue}kingtebe ${white}© 2021\n                 ƪ(‾_‾)ʃ\n\n`);
	const url = (`https://mhankbarbar.herokuapp.com/api/randomquotes`);
	request({
		url: `${url}`,
		method: `GET`,
	}, (error, response, body) => {
	if(!error && response.statusCode == 200){
		console.log(logo);
		const author = JSON.parse(body)['author']
		const quotes = JSON.parse(body)['quotes']
			console.log(` Author › ${author}`+`\n Quotes › ${quotes}\n`);
	}else{
		throw error;
		}
	});
}

quotes();
