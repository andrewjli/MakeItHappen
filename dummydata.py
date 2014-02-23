from hackkings import db
from hackkings.constants import ROLES, STATES
from hackkings.models import User,Skill,Project

sachin = User.create("sazap10", "sazap10@gmail.com", "password", ROLES.PROPOSER)
andrew = User.create("southrop", "southrop113@gmail.com", "hunter2", ROLES.DEVELOPER)
nic = User.create("nic", "nick@gmail.com", "password", ROLES.DEVELOPER)
Ilija= User.create("Ilija", "Ilija@gmail.com", "letmein", ROLES.DEVELOPER)
Microsoft=User.create("Microsoft", "windows@hotmail.com", "apple", ROLES.PROPOSER)
project = Project("Spreadsheet", "Microsoft", "Implement a spreadsheet for entering, modeling and viewing numerical data. Spreadsheet needs to have the ability to represent and evaluate symbolic expressions which are stored in, and can refer to other, cells. Cells are reffered to by a combination of their column and row names. Each cell can contain some text, reffered to as the cell's expression. A user can edit the expression in any cell, and when editing is finished, the expression is interpreted by the cell to produce the value which the cell displays. Feel free to design and structure your classes as you like, however, you may find an attached suggested design useful.", "two weeks", "intermediate")
project.add_skill("java")
db.session.commit()
someSkills = ["java", "c++","js", "c", "python", "web dev"]
skillObjects = map(Skill,someSkills);
map(db.session.add, skillObjects)
db.session.commit()
map(andrew.add_skill, skillObjects)
map(nic.add_skill, skillObjects)
map(Ilija.add_skill, skillObjects)
names = ["project", "awesome project", "even awesomer project", "super awesome project","super duper awesomer project"]
for name in names:
    project = Project(name, sachin, "some awesome project description", "9000", "0")
    project.add_skill(skillObjects[1])
    if name == "project":
    	project.add_developer(andrew)
    if name == "awesome project":
    	project.add_developer(andrew)
    	project.set_complete()
    db.session.add(project)
db.session.commit()
