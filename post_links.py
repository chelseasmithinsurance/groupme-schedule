import requests
import datetime

BOT_ID = "95126cee886c3bff49123af185"

# weekday(): Monday = 0 ... Sunday = 6
schedule = {
    0: {  # Monday
        "header": (
            "📅 *Monday Call Schedule* — Let’s start the week strong! 💪\n"
            "⭐ = Non-Negotiable Call"
        ),
        "calls": [
            {
                "title": "🔥 0% Call",
                "time": "M-F 9:30am EST",
                "description": "✅ Tap in to kickstart your morning, review your numbers, and lock in your daily focus.",
                "link": "https://us02web.zoom.us/j/2525241997#success",
            },
            {
                "title": "💬 MACC Room",
                "time": "10:00am–8:00pm EST",
                "description": "Open working room for collaboration and support.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
            {
                "title": "⭐ 🏆 Hunt/McLean Baseshop Huddle",
                "time": "12:00pm EST",
                "description": "✅ Jump on with the Hunt & McLean direct teams for a quick sync, weekly wins, and direction for the week. Please have your camera on and stay engaged throughout meeting.",
                "link": "https://us02web.zoom.us/j/86558049309?pwd=NDllTy9sdzJsY0ZpamdXSWl0cWlJZz09#success",
                "password": "baseshop!",
            },
        ],
    },

    1: {  # Tuesday
        "header": (
            "📅 *Tuesday Call Lineup* — Keep the momentum going 🚀\n"
            "⭐ = Non-Negotiable Call"
        ),
        "calls": [
            {
                "title": "🔥 0% Call",
                "time": "9:30am EST",
                "description": "✅ Tap in to kickstart your morning, review your numbers, and lock in your daily focus.",
                "link": "https://us02web.zoom.us/j/2525241997#success",
            },
            {
                "title": "💬 MACC Room",
                "time": "10:00am–8:00pm EST",
                "description": "Work together, ask questions, and stay productive.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
            {
                "title": "🌟 Top Producer Call",
                "time": "12:00pm–1:00pm EST",
                "description": "Learn directly from top performers.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
        ],
    },

    2: {  # Wednesday
        "header": (
            "📅 *Wednesday Calls* — Midweek push 💥\n"
            "⭐ = Non-Negotiable Call"
        ),
        "calls": [
            {
                "title": "🔥 0% Call",
                "time": "9:30am EST",
                "description": "✅ Tap in to kickstart your morning, review your numbers, and lock in your daily focus.",
                "link": "https://us02web.zoom.us/j/2525241997#success",
            },
            {
                "title": "💬 MACC Room",
                "time": "10:00am–8:00pm EST",
                "description": "Collaborate and stay consistent.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
            {
                "title": "🇺🇸 National Call",
                "time": "12:30pm–2:00pm EST",
                "description": "Company-wide updates and training.",
                "link": "https://zoom.us/j/571684240#success",
            },
            {
                "title": "🆕 New Agent Activation Call",
                "time": "6:00pm–7:00pm EST",
                "description": "Support and training for new agents.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
        ],
    },

    3: {  # Thursday
        "header": (
            "📅 *Thursday Growth Calls* — Level up 📈\n"
            "⭐ = Non-Negotiable Call"
        ),
        "calls": [
            {
                "title": "🔥 0% Call",
                "time": "9:30am EST",
                "description": "✅ Tap in to kickstart your morning, review your numbers, and lock in your daily focus.",
                "link": "https://us02web.zoom.us/j/2525241997#success",
            },
            {
                "title": "💬 MACC Room",
                "time": "10:00am–8:00pm EST",
                "description": "Open room for productivity and support.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
            {
                "title": "🧱 Be a Better Builder",
                "time": "10:00am–11:00am EST",
                "description": "Build stronger habits and systems.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
            {
                "title": "🧠 Getting Unstuck",
                "time": "12:00pm–1:00pm EST",
                "description": "Break through obstacles and regain momentum.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
        ],
    },

    4: {  # Friday
        "header": (
            "📅 *Friday Calls* — Finish strong 🎯\n"
            "⭐ = Non-Negotiable Call"
        ),
        "calls": [
            {
                "title": "🔥 0% Call",
                "time": "9:30am EST",
                "description": "✅ Tap in to kickstart your morning, review your numbers, and lock in your daily focus.",
                "link": "https://us02web.zoom.us/j/2525241997#success",
            },
            {
                "title": "💬 MACC Room",
                "time": "10:00am–8:00pm EST",
                "description": "Wrap up the week together with top producers and builders.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
            {
                "title": "⭐ 🏆 Hunt/McLean Baseshop Huddle",
                "time": "12:00pm EST",
                "description": "✅ Connect with the entire Hunt Master Agency as we recap the week, set up the nenxt, and celebrate wins.",
                "link": "https://us02web.zoom.us/j/83531832146?pwd=ZGZtbjFDVndjL1VQeEhVNUNMTkhsZz09#success",
                "password": "huddleup",
            },
            {
                "title": "📞 Dial Team",
                "time": "4:00pm–7:00pm EST",
                "description": "Focused dialing session to set yourself up for success.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
        ],
    },

    5: {  # Saturday
        "header": (
            "📅 *Saturday Dial Session* — Let’s build momentum 🧠📞\n"
            "⭐ = Non-Negotiable Call"
        ),
        "calls": [
            {
                "title": "📞 Dial Team",
                "time": "9:00am–12:00pm EST",
                "description": "Dedicated dialing time to get ahead for the week.",
                "link": "https://us06web.zoom.us/j/3580944678?from=join#success",
                "password": "grit",
            },
        ],
    },
}

today = datetime.datetime.utcnow().weekday()

# Skip Sunday
if today not in schedule:
    exit()

message = schedule[today]["header"] + "\n\n"

for call in schedule[today]["calls"]:
    message += f"📌 *{call['title']}*\n"
    message += f"⏰ {call['time']}\n"
    message += f"📝 {call['description']}\n"
    message += f"🔗 {call['link']}\n"
    if "password" in call:
        message += f"🔐 Password: `{call['password']}`\n"
    message += "\n"

requests.post(
    "https://api.groupme.com/v3/bots/post",
    json={
        "bot_id": BOT_ID,
        "text": message
    }
)
