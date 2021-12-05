const {
    Command
} = require('discord.js-commando', 'discord.js');

module.exports = class SayCommand extends Command {
    constructor(client) {
        super(client, {
            name: 'announce',
            group: 'meta',
            memberName: 'announce',
            description: 'Announce firmware updates.Ex: !announce iOS 11.3 db 2 ',
            examples: ['!announce 11.3 db 2'],
            args: [{
                    key: 'platform',
                    prompt: 'Which platform',
                    type: 'string'
                },
                {
                    key: 'ver',
                    prompt: 'Which version ?',
                    type: 'string'
                },
                {
                    key: 'beta',
                    prompt: 'Is it a public or a developer beta(pb or db)?',
                    type: 'string',

                },
                {
                    key: 'betaVER',
                    prompt: 'Which version of beta?',
                    type: 'integer',

                }

            ]
        });
    }
    hasPermission(msg) {
        return (msg.member.roles.exists("name", "Administrators"));
    }
    run(msg, {
        platform,
        ver,
        beta,
        betaVER
    }) {
        msg.delete();
        if (msg.channel === msg.guild.channels.find("name", "staff-botspam")) {
            if (beta === 'pb' || beta === 'db') {
                if (beta.indexOf('db') >= 0) {
                    var stringy = beta.replace("db", "Developer Beta");
                } else {
                    var stringy = beta.replace("pb", "Public Beta");
                }
                const role = msg.guild.roles.find("name", platform);
                role.setMentionable(true);
                const channel = msg.guild.channels.find("name", "announcements");
                setTimeout(() => {
                    channel.send(`${role} ${ver} ${stringy} ${betaVER} has been released`);
                    setTimeout(() => role.setMentionable(false), 1e4);

                }, 1e4)
            } else {
                console.log('Invalid Beta ');
                msg.reply(`Invalid Beta`);
            }

        }
    }
};
