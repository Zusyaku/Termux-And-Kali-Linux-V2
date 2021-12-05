const { Command } = require("discord.js-commando");
const { MessageEmbed } = require("discord.js");
const db = require("quick.db");
module.exports = class ReplyCommand extends Command {
    constructor(client) {
        super(client, {
            name: 'pirate',
            group: 'roles',
            memberName: 'pirate',
            description: 'Give or remove pirate role.',
            examples: ['pirate @oliver#9880 cydown'],
            guildOnly: true,
            args: [
                {
                    key: "member",
                    prompt: "Please specify a member.",
                    type: "member"
                },
                {
                    key: "reason",
                    prompt: "Please specify a reason",
                    type: "string",
                    default: ""
                }
            ]
        });
    }
    hasPermission(message) {
        return (message.member.roles.exists("name", "Geniuses™") || message.member.roles.exists("name", "Moderators") || message.member.roles.exists("name", "Electra Geniuses™"));
    }
    async run(message, { member, reason }) {
        message.delete();   
        if (member.roles.exists("name", "Geniuses™") || member.roles.exists("name", "Moderators")) return message.reply("You can't give a genius or moderator the pirate role!");
        const preCheck = await db.fetchObject(message.guild.id + member.user.id + "_pirate");
        const pirateReports = message.guild.channels.find("name", "pirate-reports"); //get the channel so send piratemessage to
        const pirateRole = message.guild.roles.find("name", "Pirate"); //pirate role, obv
        if (reason && preCheck.text.length == 18) return message.reply("That person is already a pirate!"); 
        if (!reason){ //remove pirate role and message if there's no reason
            member.roles.remove(member.roles.find("name", "Pirate"));                               //start by removing the role
            const data = await db.fetchObject(message.guild.id + member.user.id + "_pirate");       //get data from database 
            if (data.text === "not_pirate" || data.text == "") return  message.reply(`${member} is not a pirate!`);    //if the person isn't a pirate throw a little error message
            const pirateMessage = await pirateReports.messages.fetch(data.text);                    //fetch the message which was stored in the database
            pirateMessage.delete();                                                                 //delete the message stored in the database
            db.updateText(message.guild.id + member.user.id + "_pirate", "not_pirate");             //make sure the db knows the member isn't a pirate anymore
            /*
            let preEditArr = await db.fetchArray(message.guild.id + "_blacklisted");
            if (!includes(preEditArr, id)) return message.reply("That user or role is not blacklisted.");
            else {
                preEditArr = preEditArr.filter(e => e != member.id);
                message.reply(`Unblacklisted \`${id}\`.`);
                db.setArray(message.guild.id + "_blacklisted", preEditArr);
            }*/
            return message.reply(`removed role from ${member}.`);                                   //let the genius/mod/admin know that the role is gone
        }
        const roleArray = member.roles.array(); // discord.js has a weird way of handling role adding on master
        roleArray.push(pirateRole);             // so we just do this
        member.edit({
            roles: roleArray
        });
        db.updateValue(message.guild.id + member.user.id + "_pirate_cases", 1);
        const pirateCases = await db.fetchObject(message.guild.id + member.user.id + "_pirate_cases").then(async (e) => {
            if (e.value >= 3) {
                member.ban({ reason: "Exceeded 3 piracy cases." });
                db.updateValue(message.guild.id + member.user.id + "_pirate_cases", -3);
                message.reply("Member banned.");
            } else {
                const newPirateCase = await db.fetchObject(message.guild.id + member.user.id + "_pirate_cases");
                console.log(newPirateCase);
                const embed = new MessageEmbed()
                    .setTimestamp()
                    .setAuthor(this.client.user.username, this.client.user.displayAvatarURL())                                  //just make the embed no need to comment smh
                    .setTitle("Pirate")
                    .setDescription(`${member.user.username} (${member.user} : ${member.user.id}) is a pirate.`)
                    .addField("Reason", reason)
                    .addField("Amount of times caught", newPirateCase.value)
                    .setColor("0x36393E")
                    .setFooter(`Done by ${message.author.tag}`, message.author.displayAvatarURL())
                const m = await pirateReports.send(embed);
                member.user.send(`Hi! You got the pirate role for following reason: ${reason}\nThis means you can't send message in the Support and Current Jailbreak/Tools category.` +
                `To get this role removed, talk to a genius. Make sure you show him/her all of your tweaks, sources, and installed apps.`, {
                    files: ["https://cdn.discordapp.com/attachments/367025568685883392/430770611753713665/pirates.png"]
                });
                db.updateText(message.guild.id + member.user.id + "_pirate", m.id); //add message id to database to delete the message later
            }
        });
    }
};

function includes(arr, query) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == query) return true;        
    }
    return false;
}
