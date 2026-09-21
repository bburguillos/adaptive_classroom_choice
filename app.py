import random
from datetime import date
import streamlit as st

st.set_page_config(page_title="Ready, Set, Choose!", page_icon="🧩", layout="wide")

st.markdown("""
<style>
:root{color-scheme:light!important}.stApp{background:linear-gradient(180deg,#fffaf2,#eef7ff);color:#172033}.block-container{max-width:1150px;padding-top:1.4rem}h1,h2,h3{color:#173b65!important}.stApp p,.stApp li,.stApp label,.stApp [data-testid="stMarkdownContainer"],.stApp [data-testid="stWidgetLabel"] p{color:#172033!important}.hero,.panel,.choice{background:#fff;border:2px solid #93c5fd;border-radius:18px;padding:18px;box-shadow:0 7px 20px #1e40af14}.choice{min-height:205px;border-color:#c7d2fe}.choice h3{color:#174a7e!important}.pill{display:inline-block;border-radius:999px;background:#e0f2fe;color:#075985;padding:.2rem .55rem;margin:.12rem .15rem;font-size:.78rem;font-weight:800}.step{background:#eff6ff;border-left:5px solid #2563eb;border-radius:9px;padding:10px 13px;margin:8px 0}.adult{background:#fff7ed;border:2px solid #fdba74;border-radius:13px;padding:12px 14px}
</style>""", unsafe_allow_html=True)

def t(i,title,modes,materials,mins,goal,steps,adult,easy,hard,link):
    return dict(id=i,title=title,modes=modes,materials=materials,minutes=mins,goal=goal,steps=steps,adult=adult,easy=easy,hard=hard,link=link)

TASKS=[
 t("breathe","Trace, Breathe, and Pause",["Regulate & Focus"],["paper","pencils"],5,"Visual attention and calm breathing",["Trace a large circle slowly.","Breathe in going up and out going down.","Color the circle."],"Model one circle with a quiet voice.","Guide the hand or trace beside the student.","Add a repeating pattern inside the circle.","Use team colors if motivating."),
 t("colors","Color Sort",["Regulate & Focus","Participate"],["crayons","paper"],8,"Visual discrimination and sorting",["Draw two or three spaces.","Choose colors.","Place matching marks in the correct space."],"Offer only two colors if needed.","Use two colors and accept pointing.","Sort four colors and explain a match.","Sort sports or team colors."),
 t("same","Same or Different?",["Regulate & Focus","Participate"],["classroom objects","paper","pencils"],8,"Comparing features",["Place two objects together.","Ask same, different, or both.","Draw or point to the answer."],"Accept eye gaze, pointing, or speech.","Use only one comparison.","Name a similarity and a difference.","Compare sports pictures or numbers."),
 t("pattern","Quiet Pattern Maker",["Regulate & Focus","Participate"],["paper","markers"],10,"Repeating patterns and attention",["Make a dot-line pattern.","Continue it across the page.","Pause whenever needed."],"Start the pattern and invite one mark.","Use AB only.","Create AAB or ABB.","Use team colors or score marks."),
 t("groups","Build a Group",["Participate","Practice"],["counters","blocks","paper"],10,"Counting and grouping",["Choose a number 1–10.","Build that many objects.","Circle or write the number."],"Count together with a number card.","Use 1–5.","Make two groups and compare them.","Build a team lineup."),
 t("sticky","Sticky Note Count",["Participate","Practice"],["sticky notes","paper","pencils"],10,"Counting and recording",["Place 1–10 sticky notes.","Touch-count each one.","Choose the matching number."],"Limit the range to 1–5.","Count with an adult.","Make two amounts and compare.","Make a two-team scoreboard."),
 t("sort","Sort and Tell",["Participate","Practice"],["buttons or counters","paper"],12,"Categorizing by an attribute",["Choose color, size, or shape.","Make groups.","Tell or show the rule."],"Give the rule first.","Sort by one rule only.","Resort by a second rule.","Sort team colors or positions."),
 t("dice","Roll, Count, Compare",["Participate","Practice","Stretch"],["dice","paper","pencils"],12,"Comparing quantities",["Roll a die.","Record the number.","Roll again and show which is more."],"Use one die and dot patterns.","Compare two rolls.","Roll two dice, add, and compare.","Treat rolls as team scores."),
 t("cards","Put Cards in Order",["Participate","Practice","Stretch"],["playing cards","paper"],15,"Ordering numbers",["Choose 3–5 number cards.","Put them least to greatest.","Point to first and last."],"Use cards 1–5 only.","Order three cards.","Order seven and find the middle.","Make a finishing-order list."),
 t("blocks","Build My Model",["Participate","Practice"],["blocks"],12,"Following a visual model",["Adult builds a small model.","Student copies it.","Compare the models."],"Use two blocks.","Match color or position.","Student gives directions to rebuild it.","Build a stadium or podium."),
 t("clayshape","Clay Shape Shop",["Participate","Practice","Stretch"],["clay or Play-Doh","paper"],15,"Fine-motor work and shapes",["Make a ball, snake, and pancake.","Match each to a drawing.","Decorate one."],"Adult rolls clay if needed.","Make one shape.","Make a triangle or pattern.","Make a ball, jersey, trophy, or number."),
 t("claynum","Make the Number",["Participate","Practice"],["clay or Play-Doh","paper"],12,"Number recognition",["Choose a number.","Roll a clay snake.","Form and trace the number."],"Use one large number.","Copy an adult-made number.","Make two and compare them.","Make a favorite jersey number."),
 t("measure","Measure Classroom Objects",["Practice","Stretch"],["ruler","pencils","paper","classroom objects"],15,"Comparing length",["Choose three safe objects.","Measure each.","Record or draw short, medium, long."],"Use comparison words instead of numbers.","Choose short and long.","Order measurements and find a difference.","Compare cards or score sheets."),
 t("graph","Sticker or Mark Graph",["Practice","Stretch"],["paper","sticky notes","pencils"],15,"Representing categories",["Choose 2–3 answer categories.","Ask a question.","Add one mark per answer."],"Use two categories and adult answers.","Make two columns.","Label and find the most.","Graph favorite sports or colors."),
 t("frequency","Make a Counting Table",["Practice","Stretch"],["paper","pencils","counters"],18,"Organizing category counts",["Draw category boxes.","Place one counter per item.","Count and record totals."],"Adult draws boxes and names categories.","Use two categories.","Compare categories with counts.","Make a one-way frequency table."),
 t("sequence","What Comes Next?",["Participate","Practice","Stretch"],["index cards","markers","paper"],12,"Sequencing",["Draw three routine steps.","Mix the cards.","Put them in order."],"Use gestures or pictures.","Use two steps.","Create a four- or five-step sequence.","Sequence a game or scoring routine."),
 t("collage","My Choice Collage",["Participate","Practice"],["paper","crayons","markers","glue"],20,"Communicating preferences",["Choose three things you like.","Draw or write them.","Arrange them on one page."],"Offer two options at a time.","Choose one thing.","Sort like, unsure, and not for me.","Include sports, teams, numbers, or colors."),
 t("hunt","Classroom Number Hunt",["Participate","Practice","Stretch"],["paper","pencils","classroom objects"],15,"Recognizing numbers",["Find three classroom numbers.","Point, copy, or draw them.","Put them in order."],"Adult points out the first.","Find one number.","Find five and identify greatest.","Find numbers on books or calendars."),
 t("story","Roll a Tiny Story",["Practice","Stretch"],["dice","paper","pencils"],15,"Using numbers in a story",["Roll for how many objects.","Roll for more or fewer.","Draw and solve with counters."],"Adult narrates the story.","Use addition within 5.","Write a sports score story.","Use a team score narrative."),
 t("draw","Listen and Draw",["Participate","Practice"],["paper","pencils","crayons"],12,"Following directions",["Complete one drawing direction.","Add a second direction.","Show the finished picture."],"Use gestures and model after trying.","Follow one direction.","Follow three linked directions.","Draw a court or scoreboard."),
 t("tally","Quiet Tally Marks",["Regulate & Focus","Participate"],["paper","pencils"],8,"Repeated motor action and counting",["Make groups of five tally marks.","Pause after each group.","Count the total."],"Dots may replace tally marks.","Make one group.","Record two groups and compare.","Tally colors, teams, or symbols."),
 t("free","Build Something You Choose",["Regulate & Focus","Participate","Practice"],["clay or Play-Doh"],15,"Choice and sustained engagement",["Choose what to build.","Build for five minutes.","Show or name one part."],"Offer two ideas if needed.","Copy a simple model.","Use patterns or named shapes.","Build a sports object or trophy."),
 t("symbols","Letter or Number Sort",["Regulate & Focus","Participate"],["index cards","markers","paper"],10,"Visual sorting",["Write or use letter and number cards.","Make two groups.","Place each card correctly."],"Use three cards at a time.","Sort letters and numbers.","Sort odd/even or vowels/consonants.","Use jersey numbers and initials."),
 t("target","Draw the Target",["Regulate & Focus","Participate","Practice"],["paper","markers","pencils"],12,"Visual-motor control",["Draw a three-section target.","Color each section.","Point to center and outside."],"Adult draws the target first.","Color two sections.","Add point values and choose a score.","Use sports-style point values."),
 t("reset","Choose Your Reset",["Regulate & Focus"],["paper","crayons"],5,"Communicating a regulation preference",["Choose draw, breathe, stretch, or quiet look.","Do it for two minutes.","Show finished, more, or stop."],"Honor the choice and keep language minimal.","Adult offers two choices.","Student leads the adult through the reset.","Decorate a team-color breathing card."),
]

MODE_INFO={"Regulate & Focus":"Short, calm tasks for attention, communication, and readiness.","Participate":"Simple hands-on tasks with choices and adult guidance.","Practice":"Academic or classroom-skill practice with a clear product.","Stretch":"More independent, multi-step tasks with optional sports/math connections."}

def compatible(mode,materials,minutes):
    items=[x for x in TASKS if mode in x["modes"] and x["minutes"]<=minutes]
    if materials: items=[x for x in items if set(x["materials"]).issubset(set(materials))]
    return items

def card(item,n):
    return f"<div class='choice'><span class='pill'>{item['minutes']} min</span><span class='pill'>{', '.join(item['materials'])}</span><h3>{n}. {item['title']}</h3><p><b>Goal:</b> {item['goal']}</p><p><b>Connection:</b> {item['link']}</p></div>"

st.markdown("<div class='hero'><h1>🧩 Ready, Set, Choose!</h1><p>A flexible classroom activity tool for choosing a task that fits today.</p><p>The adult chooses the readiness mode. The student still gets meaningful choices.</p></div>",unsafe_allow_html=True)
st.sidebar.header("👩‍🏫 Adult Setup")
mode=st.sidebar.selectbox("Today’s readiness mode",list(MODE_INFO),key="mode")
st.sidebar.info(MODE_INFO[mode])
minutes=st.sidebar.slider("Available time",5,30,15,step=5)
all_materials=sorted({m for x in TASKS for m in x["materials"]})
materials=st.sidebar.multiselect("Materials available today",all_materials,default=["paper","pencils","crayons","markers"])
show_sports=st.sidebar.checkbox("Show sports/math connections",value=True)
student=st.sidebar.text_input("Student name or initials (optional)")

st.markdown("### Student choice")
st.write("Choose one of the activities below. You can change your mind before starting.")
options=compatible(mode,materials,minutes)
if not options:
    st.warning("No tasks match every selected filter. Add a material or increase the time.")
    st.stop()
if "seed" not in st.session_state: st.session_state.seed=random.randrange(100000)
if st.button("🔄 Give me three different choices",use_container_width=True): st.session_state.seed=random.randrange(100000)
shown=random.Random(st.session_state.seed).sample(options,min(3,len(options)))
cols=st.columns(len(shown))
for n,(col,item) in enumerate(zip(cols,shown),1):
    with col:
        st.markdown(card(item,n),unsafe_allow_html=True)
        if st.button(f"Choose {n}",key=f"choose_{item['id']}",use_container_width=True): st.session_state.selected=item["id"]

selected=next((x for x in TASKS if x["id"]==st.session_state.get("selected")),None)
if selected is None:
    st.info("Choose an activity to see the directions.")
    st.stop()
st.markdown("---")
st.markdown(f"<div class='panel'><h2>✅ {selected['title']}</h2><p><b>Goal:</b> {selected['goal']}</p><p><b>Materials:</b> {', '.join(selected['materials'])}</p></div>",unsafe_allow_html=True)
st.markdown("### Steps for the student")
for n,step in enumerate(selected["steps"],1): st.markdown(f"<div class='step'><b>{n}.</b> {step}</div>",unsafe_allow_html=True)
st.markdown("### Adult support")
st.markdown(f"<div class='adult'>{selected['adult']}</div>",unsafe_allow_html=True)
if show_sports: st.info(f"🏅 Optional connection: {selected['link']}")
with st.expander("Adjust the task without changing the student’s choice"):
    st.write(f"**Make it easier:** {selected['easy']}")
    st.write(f"**Add challenge:** {selected['hard']}")

st.markdown("### Quick check-in")
status=st.radio("How did it go?",["Not started","Working","Finished","Needed a break"],horizontal=True)
notes=st.text_area("Optional adult note",placeholder="What helped? What should we try next time?")
if st.button("✅ Save today’s check-in",use_container_width=True):
    st.session_state.last_checkin={"date":date.today().isoformat(),"student":student or "Student","mode":mode,"task":selected["title"],"status":status,"notes":notes}
    st.success("Today’s check-in was saved for this session.")
if st.session_state.get("last_checkin"):
    x=st.session_state.last_checkin
    st.caption(f"Last check-in: {x['task']} · {x['status']} · {x['date']}")
