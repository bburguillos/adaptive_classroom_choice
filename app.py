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

# The first bank above contains reusable prototypes. This student-facing bank
# replaces vague directions with concrete quantities, materials, and finish lines.
def detailed(item, finish=None):
    # Detailed tasks store their completion sentence in the final `t()` field.
    # Accepting it here keeps every task entry compact and prevents deployment errors.
    if finish is None:
        finish = item["link"]
        item["link"] = "Use sports colors, scores, or team names only if that helps motivate the student."
    item["finish"] = finish
    return item

TASKS = [
 detailed(t("crayon_sort","Sort 12 Crayons",["Regulate & Focus","Participate"],["paper","crayons"],15,"Sort objects by color and count each group",["Get 12 crayons: 4 red, 4 blue, and 4 yellow.","Draw 3 large circles on a piece of paper.","Write RED, BLUE, and YELLOW above the circles.","Put each crayon in the circle with the same color.","Touch-count the crayons in each circle and tell the adult the numbers."],"Put the 12 crayons in a small pile. Point to one crayon at a time and help only when needed.","Use 6 crayons: 2 red, 2 blue, and 2 yellow.","Write the total number of crayons in all 3 circles.","This is finished when every crayon is in a labeled circle and each group has a number.")),
 detailed(t("block_towers","Build 3 Block Towers",["Participate","Practice"],["blocks","paper","pencils"],15,"Count blocks and compare tower heights",["Get 6 blocks.","Build Tower 1 with 1 block.","Build Tower 2 with 2 blocks.","Build Tower 3 with 3 blocks.","Draw the 3 towers on paper.","Circle the tallest tower."],"Place one block at a time beside the student and count aloud.","Build only Tower 1 and Tower 2.","Build a fourth tower with 4 blocks and label it.","This is finished when 3 towers are standing, drawn, and the tallest is circled.")),
 detailed(t("dice_tally","Roll a Die 10 Times",["Participate","Practice"],["dice","paper","pencils"],15,"Record results with tally marks",["Draw 6 boxes on paper and label them 1, 2, 3, 4, 5, and 6.","Roll the die 10 times.","After each roll, make one tally mark in the matching box.","Count the tally marks in every box.","Circle the box with the most marks."],"Roll the die for the student and let the student place each tally.","Roll 5 times using only numbers 1–3 if needed.","Roll 20 times and write the total in each box.","This is finished when 10 rolls are recorded and the box with the most is circled.")),
 detailed(t("clay_shapes","Make 3 Clay Shapes",["Participate","Practice"],["clay or Play-Doh","paper","pencils"],15,"Make and identify basic shapes",["Get 3 small pieces of clay.","Make Piece 1 into a ball.","Make Piece 2 into a long snake.","Flatten Piece 3 into a pancake.","Draw the ball, snake, and pancake on paper.","Point to each shape when the adult names it."],"Make one shape at a time and demonstrate before asking the student to copy.","Make only a ball and a snake.","Use clay to make a triangle, square, and circle.","This is finished when all 3 clay shapes are made and matched to drawings.")),
 detailed(t("card_order","Put Number Cards 1–10 in Order",["Participate","Practice","Stretch"],["playing cards","paper"],20,"Put numbers in order from smallest to largest",["Take the cards A, 2, 3, 4, 5, 6, 7, 8, 9, and 10.","Use A as the number 1.","Place all 10 cards face up.","Move the cards until they show 1 through 10 in order.","Point to the first card and say 1.","Point to the last card and say 10."],"Remove face cards and help the student find the next number.","Use only cards A through 5.","Turn the cards face down, choose 5, and put them in order from memory.","This is finished when the 10 cards show 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.")),
 detailed(t("counter_match","Match Numbers to Counters",["Participate","Practice"],["paper","pencils","counters"],15,"Match a written number to an amount",["Write the numbers 1, 2, 3, 4, and 5 in 5 boxes.","Put 1 counter under the 1.","Put 2 counters under the 2.","Continue until every number has its matching amount.","Touch-count each row."],"Make the boxes and count the first row with the student.","Use only numbers 1, 2, and 3.","Make a second set using numbers 6 through 10.","This is finished when all 5 numbers have the correct number of counters underneath.")),
 detailed(t("measure_pencils","Measure 3 Pencils",["Practice","Stretch"],["ruler","pencils","paper"],15,"Measure objects and compare lengths",["Get 3 pencils.","Line each pencil up with the zero on the ruler.","Write the length of each pencil in inches.","Draw the 3 pencils from shortest to longest.","Circle the longest pencil."],"Hold the ruler steady and accept short, medium, and long if numbers are difficult.","Compare only 2 pencils.","Find how many inches longer the longest pencil is than the shortest.","This is finished when all 3 pencils have measurements and the longest is circled.")),
 detailed(t("sticky_graph","Make a 2-Column Color Graph",["Practice","Stretch"],["paper","sticky notes","pencils"],20,"Make a simple graph from 10 choices",["Draw 2 columns on paper and label them RED and BLUE.","Get 10 sticky notes.","Place 4 notes in RED and 6 notes in BLUE.","Count the notes in each column.","Write the number at the bottom of each column.","Circle the column with more notes."],"Use 2 notes in each column first, then add more.","Use 2 red and 2 blue notes.","Ask classmates for their real color choices and graph the answers.","This is finished when both columns are labeled, counted, and the larger column is circled.")),
 detailed(t("pattern_blocks","Copy an A-B Block Pattern",["Regulate & Focus","Participate","Practice"],["blocks","paper","pencils"],15,"Copy and continue a repeating pattern",["Get 6 blocks: 3 of one color and 3 of another color.","Adult builds a pattern: red, blue, red, blue.","Copy the first 4 blocks.","Add 2 more blocks to continue the pattern.","Draw the finished pattern on paper."],"Use only 2 blocks first and let the student copy one pair.","Copy red-blue once.","Make an A-B-B pattern and explain what comes next.","This is finished when the student copies 4 blocks, adds 2, and draws the pattern.")),
 detailed(t("draw_shapes","Draw 5 Shapes from Directions",["Participate","Practice"],["paper","pencils","crayons"],15,"Follow short directions and identify shapes",["Draw 1 large circle.","Draw 1 square under the circle.","Draw 1 triangle beside the square.","Draw 1 star above the circle.","Draw 1 rectangle next to the triangle.","Color the circle blue and the square red."],"Give one direction, wait, then give the next direction.","Draw only the circle, square, and triangle.","Add position words such as left, right, above, and below.","This is finished when all 5 shapes are present and the circle and square are colored.")),
 detailed(t("button_sort","Sort 10 Buttons by Size",["Regulate & Focus","Participate"],["buttons or counters","paper"],15,"Sort objects into big and small groups",["Get 10 buttons: 5 big and 5 small.","Draw 2 circles on paper.","Label one circle BIG and one circle SMALL.","Place each button in the correct circle.","Count the buttons in each circle."],"Use 4 buttons and physically show the size difference.","Sort 2 big and 2 small buttons.","Sort the same buttons by color after sorting by size.","This is finished when all 10 buttons are in a labeled circle and both groups are counted.")),
 detailed(t("frequency_table","Make a 1-Way Counting Table",["Practice","Stretch"],["paper","pencils","counters"],20,"Separate categories and record frequencies",["Draw 3 rows labeled STAR, CIRCLE, and TRIANGLE.","Get 10 counters: 4 star cards, 3 circle cards, and 3 triangle cards.","Put each counter in the matching row.","Count each row.","Write the count next to each label.","Circle the row with the greatest count."],"Draw the rows and place one item at a time with the student.","Use 2 categories with 2 items each.","Add a total row and check that the total is 10.","This is finished when all 10 items are sorted, counted, and recorded.")),
 detailed(t("clay_number","Make and Match 3 Numbers",["Participate","Practice"],["clay or Play-Doh","paper","pencils"],15,"Form numbers and match them to written numbers",["Write 3, 6, and 9 on paper.","Make a clay snake.","Use the snake to form the number 3.","Make the number 6.","Make the number 9.","Place each clay number beside its matching written number."],"Make one number at a time and use a large model.","Make only the number 3.","Make numbers 3, 6, 9, and put them from least to greatest.","This is finished when clay 3, 6, and 9 are next to the matching written numbers.")),
 detailed(t("choice_collage","Make a 3-Choice Page",["Participate","Practice"],["paper","crayons","markers","glue"],20,"Show preferences through a clear choice",["Draw 3 large boxes on paper.","Choose 1 favorite color, 1 favorite number, and 1 favorite sport or activity.","Draw one choice in each box.","Color each drawing.","Tell or point to the choice you like best."],"Offer two choices for each box and let the student point.","Complete only the favorite-color box.","Write a sentence under each drawing with adult help.","This is finished when all 3 boxes contain a colored choice.")),
 detailed(t("calm_tally","Make 5 Groups of 5 Tally Marks",["Regulate & Focus","Participate"],["paper","pencils"],15,"Use repeated marks and count groups",["Draw 5 boxes on paper.","Put 5 tally marks in Box 1.","Put 5 tally marks in Box 2.","Repeat until all 5 boxes have 5 marks.","Touch-count one box with the adult."],"Make one box at a time and offer a short pause between boxes.","Make 2 boxes with 5 marks each.","Count all 25 marks and write 25.","This is finished when all 5 boxes have exactly 5 marks.")),
]

MODE_INFO={"Regulate & Focus":"Short, calm tasks for attention, communication, and readiness.","Participate":"Simple hands-on tasks with choices and adult guidance.","Practice":"Academic or classroom-skill practice with a clear product.","Stretch":"More independent, multi-step tasks with optional sports/math connections."}

def compatible(mode,materials,minutes):
    items=[x for x in TASKS if mode in x["modes"] and x["minutes"]<=minutes]
    if materials: items=[x for x in items if set(x["materials"]).issubset(set(materials))]
    return items

def card(item,n):
    return f"<div class='choice'><span class='pill'>{item['minutes']} min</span><span class='pill'>{', '.join(item['materials'])}</span><h3>{n}. {item['title']}</h3><p><b>Goal:</b> {item['goal']}</p><p><b>Finish:</b> {item['finish']}</p></div>"

st.markdown("<div class='hero'><h1>🧩 Ready, Set, Choose!</h1><p>A flexible classroom activity tool for choosing a task that fits today.</p><p>The adult chooses the readiness mode. The student still gets meaningful choices.</p></div>",unsafe_allow_html=True)
st.sidebar.header("👩‍🏫 Adult Setup")
mode=st.sidebar.selectbox("Today’s readiness mode",list(MODE_INFO),key="mode")
st.sidebar.info(MODE_INFO[mode])
minutes=st.sidebar.slider("Available time",15,30,20,step=5)
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
st.markdown(f"<div class='panel'><h2>✅ {selected['title']}</h2><p><b>Goal:</b> {selected['goal']}</p><p><b>Materials:</b> {', '.join(selected['materials'])}</p><p><b>You are finished when:</b> {selected['finish']}</p></div>",unsafe_allow_html=True)
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
