const { Command } = require("discord.js-commando");
const { MessageEmbed } = require("discord.js");
module.exports = class ReplyCommand extends Command {
    constructor(client) {
        super(client, {
            name: 'feedback',
            group: 'meta',
            memberName: 'feedback',
            description: 'Let the staff know of an issue.',
            examples: ['feedback "!give myrole" crashes bot'],
            throttling: {
                usages: 1,
                duration: 86400
            },
            args: [
                {
                    key: 'text',
                    prompt: "What problem are you facing?",
                    type: 'string'
                }
            ]
        });
    }

    async run(message, { text }) {
        var issuechannel = this.client.channels.get("409796293116821515");
        var report = message.author.tag + " reported an issue";
        var reportembed = new MessageEmbed()
            .setTimestamp()
            .setAuthor(this.client.user.username, this.client.user.displayAvatarURL())
            .setTitle("Someone reported an issue!")
            .addField("Description", text)
        issuechannel.send(reportembed);
    }
};
