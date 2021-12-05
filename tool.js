const { Command } = require('discord.js-commando', 'discord.js');

module.exports = class SayCommand extends Command {
    constructor(client) {
        super(client, {
            name: 'jb',
            group: 'meta',
            memberName: 'jbannounce',
            description: 'Announce jailbreak updates.Ex:!jb g0blin https://twitter.com/coolstarorg/status/961770596219539456',
            examples: ['!jb g0blin https://twitter.com/coolstarorg/status/961770596219539456.'],
            args: [
                {
                    key: 'jb',
                    prompt: 'Which role should I ping?',
                    type: 'string'
                },
                {
                    key: 'tweet',
                    prompt: 'tweet link pls?',
                    type: 'string'
                }
            ]
        });    
    }
    hasPermission(msg) {
        return (msg.member.roles.exists("name", "Administrators"));
    }
    run(msg, { jb, tweet}) {
		msg.delete(); 
		if (msg.channel !== msg.guild.channels.find("name", "staff-botspam")) return;
		const role = msg.guild.roles.find("name", jb);
        role.setMentionable(true);
        setTimeout(() => {
            const channel = msg.guild.channels.find("name", "announcements"); 
            console.log(channel);
            channel.send(`${role}  ${tweet} `);
            setTimeout(() => {
                role.setMentionable(false);
            }, 1e4);
        }, 1e4);

    }
};
