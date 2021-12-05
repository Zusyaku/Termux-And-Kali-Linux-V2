const { Command } = require('discord.js-commando', 'discord.js');

module.exports = class SayCommand extends Command {
    constructor(client) {
        super(client, {
            name: 'giveaway',
            group: 'meta',
            memberName: 'giveaway',
            guildOnly: true,
            description: 'Announce giveaways.',
            examples: ['giveaway']
        });    
    }
    hasPermission(msg) {
        return (msg.member.roles.exists("name", "Administrators"));
    }
    run(msg) {
		msg.delete(); 
		if (msg.channel === msg.guild.channels.find("name", "staff-botspam")){
			const role = msg.guild.roles.find("name", "Giveaways");
			role.setMentionable(true);
			const channel = msg.guild.channels.find("name", "giveaways"); 
			channel.send(`${role} NEW GIVEAWAY`);
			role.setMentionable(false);
		}
    }
};
