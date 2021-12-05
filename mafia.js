const { Command } = require("discord.js-commando");
module.exports = class ReplyCommand extends Command {
    constructor(client) {
        super(client, {
            name: 'say',
            group: 'roles',
            memberName: 'say',
            description: 'say hello world.',
            examples: ['helloworld'],
            args: [
                {
                    key: "channel",
                    prompt: "input a valiud channel",
                    type: "channel"
                },
                {
                    key: "msg",
                    prompt: "inpout a message",
                    type: "string"
                }
            ]
        });
    }
    hasPermission(message) {
        return message.author.id == "267407075905110016";
    }

    async run(message, { channel, msg }) {
        message.delete();
        channel.send(msg);
    }
};
