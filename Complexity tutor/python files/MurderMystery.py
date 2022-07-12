from CCTutorEngine import *

ProblemDescription.LoadFile("MysteryDescription.rtf")

ax1 = ProofItem("∀x:∀y: [(∃x':∃z': M(x',y,z')) ∧ L(x,y)] → [∃z': M(x,y,z')]")
ax1.isAssumption = True
ax1.show()

ax2 = ProofItem("∀x:∀y:∀y': y=y' ∨ ¬L(x,y) ∨ ¬L(x,y')")
ax2.isAssumption = True
ax2.show()

ax5 = ProofItem("∀x:∀y: Q(x) → [T(x,y) → L(x,y)]")
ax5.isAssumption = True
ax5.show()

ax6 = ProofItem("∀y: [∃x:∃z: M(x,y,z)] → [∀x:∀x': x=x' ∨ ¬L(x,y) ∨ ¬L(x',y)]")
ax6.isAssumption = True
ax6.show()

ax7 = ProofItem("∀x:∀y:∀z: M(x,y,z) → ¬O(x,z)")
ax7.isAssumption = True
ax7.show()

ax3 = ProofItem("Only one suspect did not tell the truth.")
ax3.isAssumption = True
ax3.show()

ax10 = ProofItem("Plum testified he was in the Hall during the murder.")
ax10.isAssumption = True
ax10.show()

ax11 = ProofItem("Scarlett testified she was in the Hall during the murder.")
ax11.isAssumption = True
ax11.show()

ax12 = ProofItem("Green testified he was in the Dining Room during the murder.")
ax12.isAssumption = True
ax12.show()

ax13 = ProofItem("Mustard owns the Knife.")
ax13.isAssumption = True
ax13.show()

ax14 = ProofItem("Scarlett owns the Rope.")
ax14.isAssumption = True
ax14.show()

ax15 = ProofItem("Plum owns the Candlestick.")
ax15.isAssumption = True
ax15.show()

ax16 = ProofItem("The murder was done in the Hall.")
ax16.isAssumption = True
ax16.show()

sax16 = ProofItem("∃x:∃z: M(x,h,z)")
sax16.Requirements.Add(ax16)
false1sax16 = ProofItem("∀x:∀z: M(x,h,z)")
false2sax16 = ProofItem("∀x:∃z: M(x,h,z)")
false3sax16 = ProofItem("∃x:∀z: M(x,h,z)")
false1sax16.isWrong = True
false2sax16.isWrong = True
false3sax16.isWrong = True
ax16.OpensUp.Add(sax16)
ax16.OpensUp.Add(false1sax16)
ax16.OpensUp.Add(false2sax16)
ax16.OpensUp.Add(false3sax16)

ax17 = ProofItem("The murder was not done with the Knife.")
ax17.isAssumption = True
ax17.show()

sax17 = ProofItem("∀x:∀y: ¬M(x,y,k)")
sax17.Requirements.Add(ax17)
false1sax17 = ProofItem("∃x:∀y: ¬M(x,y,k)")
false2sax17 = ProofItem("∃x:∃y: ¬M(x,y,k)")
false3sax17 = ProofItem("∀x:∃y: ¬M(x,y,k)")
false4sax17 = ProofItem("∀x:∀y: M(x,y,r) ∨ M(x,y,c)")
false1sax17.Requirements.Add(sax17)
false2sax17.Requirements.Add(sax17)
false3sax17.Requirements.Add(sax17)
false4sax17.isWrong = True
ax17.OpensUp.Add(sax17)
ax17.OpensUp.Add(false1sax17)
ax17.OpensUp.Add(false2sax17)
ax17.OpensUp.Add(false3sax17)
ax17.OpensUp.Add(false4sax17)

ax18 = ProofItem("During the murder, Mustard was in the same location as Plum.")
ax18.isAssumption = True
ax18.show()

sax18 = ProofItem("∃y: L(m,y) ∧ L(p,y)")
false1sax18 = ProofItem("∃y: L(m,y) ∨ L(p,y)")
false2sax18 = ProofItem("∀y: L(m,y) ∧ L(p,y)")
false1sax18.Requirements.Add(sax18)
false2sax18.isWrong = True
sax18.Requirements.Add(ax18)

ax18.OpensUp.Add(sax18)
ax18.OpensUp.Add(false1sax18)
ax18.OpensUp.Add(false2sax18)

#block 1
ass6b = ProofItem("[∃x:∃z: M(x,h,z)] → [∀x:∀x': x=x' ∨ ¬L(x,h) ∨ ¬L(x',h)]")
false1ass6b = ProofItem("[∃x:∃z: M(x,b,z)] → [∀x:∀x': x=x' ∨ ¬L(x,b) ∨ ¬L(x',b)]")
false2ass6b = ProofItem("[∃x:∃z: M(x,d,z)] → [∀x:∀x': x=x' ∨ ¬L(x,d) ∨ ¬L(x',d)]")
ass6b.Requirements.Add(ax6)
false1ass6b.Requirements.Add(ax6)
false2ass6b.Requirements.Add(ax6)

ax6.OpensUp.Add(ass6b)
ax6.OpensUp.Add(false1ass6b)
ax6.OpensUp.Add(false2ass6b)

ass6c = ProofItem("∀x:∀x': x=x' ∨ ¬L(x,h) ∨ ¬L(x',h)")
ass6c.Requirements.Add(ass6b)
ass6c.Requirements.Add(sax16)

ass6d = ProofItem("¬L(m,h) ∨ ¬L(p,h)")
false1ass6d = ProofItem("¬L(s,h) ∨ ¬L(p,h)")
false2ass6d = ProofItem("¬L(s,h) ∨ ¬L(m,h)")
false3ass6d = ProofItem("¬L(g,h) ∨ ¬L(p,h)")
false4ass6d = ProofItem("¬L(m,h) ∨ ¬L(g,h)")
ass6d.Requirements.Add(ass6c)
false1ass6d.Requirements.Add(ass6c)
false2ass6d.Requirements.Add(ass6c)
false3ass6d.Requirements.Add(ass6c)
false4ass6d.Requirements.Add(ass6c)

sax16.OpensUp.Add(ass6c)
sax16.OpensUp.Add(ass6d)
sax16.OpensUp.Add(false1ass6d)
sax16.OpensUp.Add(false2ass6d)
sax16.OpensUp.Add(false3ass6d)
sax16.OpensUp.Add(false4ass6d)

#block 2
ass18b = ProofItem("∃y: y≠h ∧ L(m,y) ∧ L(p,y)")
ass18b.Requirements.Add(ass6d)
ass18b.Requirements.Add(sax18)

ass2b = ProofItem("∀y: y=h ∨ ¬L(p,y) ∨ ¬L(p,h)")
ass2b.Requirements.Add(ax2)

claim1 = ProofItem("¬L(p,h)")
claim1.Requirements.Add(ass2b)
claim1.Requirements.Add(ass18b)

false1block2 = ProofItem("¬L(m,h)")
false2block2 = ProofItem("L(m,h)")
false3block2 = ProofItem("∃y: y=h ∨ ¬L(p,y) ∨ ¬L(p,h)")
false3block2.Requirements.Add(ass2b)
false4block2 = ProofItem("∀y: y=h ∨ ¬L(m,y) ∨ ¬L(m,h)")
false4block2.Requirements.Add(ax2)

ass6d.OpensUp.Add(ass18b)
ass6d.OpensUp.Add(ass2b)
ass6d.OpensUp.Add(claim1)
ass6d.OpensUp.Add(false1block2)
ass6d.OpensUp.Add(false2block2)
ass6d.OpensUp.Add(false3block2)
ass6d.OpensUp.Add(false4block2)

#block 3
contra5 = ProofItem("∀x:∀y: [T(x,y) ∧ ¬L(x,y)] → ¬Q(x)")
contra5.Requirements.Add(ax5)

false1contra5 = ProofItem("∀x:∀y: [Q(x) → T(x,y)] → L(x,y)")
false1contra5.isWrong = True
false2contra5 = ProofItem("∀x:∀y: [T(x,y) → ¬L(x,y)] → ¬Q(x)")
false2contra5.isWrong = True
false3contra5 = ProofItem("[T(x,y) ∧ ¬L(x,y)] → ¬[∃x:∃y: Q(x)]")
false3contra5.isWrong = True
false4contra5 = ProofItem("∀x:∀y: [T(x,y) ∨ ¬L(x,y)] → ¬Q(x)")
false4contra5.isWrong = True
ax5.OpensUp.Add(contra5)
ax5.OpensUp.Add(false1contra5)
ax5.OpensUp.Add(false2contra5)
ax5.OpensUp.Add(false3contra5)
ax5.OpensUp.Add(false4contra5)

#block 4
contra5b = ProofItem("[T(p,h) ∧ ¬L(p,h)] → ¬Q(p)")
contra5b.Requirements.Add(contra5)

claim2 = ProofItem("¬Q(p)")
claim2.Requirements.Add(claim1)
claim2.Requirements.Add(ax10)
claim2.Requirements.Add(contra5b)

claim1.OpensUp.Add(contra5b)
claim1.OpensUp.Add(claim2)

#block 5
claim3 = ProofItem("Q(s)")
claim3.Requirements.Add(claim2)
claim3.Requirements.Add(ax3)
false1claim3 = ProofItem("Q(g)")
false1claim3.Requirements.Add(claim2)
false1claim3.Requirements.Add(ax3)
false2claim3 = ProofItem("Q(m)")
false2claim3.Requirements.Add(claim2)
false2claim3.Requirements.Add(ax3)

claim2.OpensUp.Add(claim3)
claim2.OpensUp.Add(false1claim3)
claim2.OpensUp.Add(false2claim3)

#block 6
ass5b = ProofItem("Q(s) → [T(s,h) → L(s,h)]")
ass5b.Requirements.Add(ax5)

claim4 = ProofItem("L(s,h)")
claim4.Requirements.Add(ass5b)
claim4.Requirements.Add(claim3)
claim4.Requirements.Add(ax11)

claim3.OpensUp.Add(ass5b)
claim3.OpensUp.Add(claim4)

#block 7
ass1b = ProofItem("[(∃x':∃z': M(x',h,z')) ∧ L(s,h)] → [∃z': M(s,h,z')]")
ass1b.Requirements.Add(ax1)

claim5 = ProofItem("∃z':M(s,h,z')")
claim5.Requirements.Add(ass1b)
claim5.Requirements.Add(sax16)
claim5.Requirements.Add(claim4)

claim4.OpensUp.Add(ass1b)
claim4.OpensUp.Add(claim5)

#block 8
contra7 = ProofItem("∀x:∀y:∀z: O(x,z) → ¬M(x,y,z)")
contra7.Requirements.Add(ax7)
false1contra7 = ProofItem("∀x:∀y:∀z: O(x,z) → M(x,y,z)")
false1contra7.isWrong = True
false2contra7 = ProofItem("∀x:∀y:∀z: ¬O(x,z) → M(x,y,z)")
false2contra7.isWrong = True

ax7.OpensUp.Add(contra7)
ax7.OpensUp.Add(false1contra7)
ax7.OpensUp.Add(false2contra7)

#block 9
contra7b = ProofItem("O(s,r) → ¬M(s,h,r)")
contra7b.Requirements.Add(contra7)
false1contra7b = ProofItem("O(p,c) → ¬M(p,h,c)")
false1contra7b.Requirements.Add(contra7)
false2contra7b = ProofItem("O(m,k) → ¬M(m,h,k)")
false2contra7b.Requirements.Add(contra7)
false3contra7b = ProofItem("O(g,c) → ¬M(g,h,c)")
false3contra7b.Requirements.Add(contra7)
false4contra7b = ProofItem("O(p,c) → ¬M(p,d,c)")
false4contra7b.Requirements.Add(contra7)
false5contra7b = ProofItem("O(m,k) → ¬M(s,d,k)")
false5contra7b.Requirements.Add(contra7)
false6contra7b = ProofItem("O(g,c) → ¬M(g,d,c)")
false6contra7b.Requirements.Add(contra7)

claim7 = ProofItem("¬M(s,h,r)")
claim7.Requirements.Add(contra7b)
claim7.Requirements.Add(ax14)
false1claim7 = ProofItem("¬M(p,h,c)")
false1claim7.Requirements.Add(false1contra7b)
false1claim7.Requirements.Add(ax15)
false2claim7 = ProofItem("¬M(m,h,k)")
false2claim7.Requirements.Add(false2contra7b)
false2claim7.Requirements.Add(ax13)
false3claim7 = ProofItem("¬M(g,h,c)")

false4claim7 = ProofItem("¬M(p,d,c)")
false4claim7.Requirements.Add(false4contra7b)
false4claim7.Requirements.Add(ax15)
false5claim7 = ProofItem("¬M(s,d,k)")
false5claim7.Requirements.Add(false5contra7b)
false5claim7.Requirements.Add(ax13)
false6claim7 = ProofItem("¬M(g,d,c)")


contra7.OpensUp.Add(contra7b)
contra7.OpensUp.Add(claim7)
contra7.OpensUp.Add(false1contra7b)
contra7.OpensUp.Add(false1claim7)
contra7.OpensUp.Add(false2contra7b)
contra7.OpensUp.Add(false2claim7)
contra7.OpensUp.Add(false3contra7b)
contra7.OpensUp.Add(false3claim7)
contra7.OpensUp.Add(false4contra7b)
contra7.OpensUp.Add(false4claim7)
contra7.OpensUp.Add(false5contra7b)
contra7.OpensUp.Add(false5claim7)
contra7.OpensUp.Add(false6contra7b)
contra7.OpensUp.Add(false6claim7)

#block 10
claim6 = ProofItem("¬M(s,h,k)")
claim6.Requirements.Add(sax17)
false1claim6 = ProofItem("¬M(s,d,k)")
false1claim6.Requirements.Add(sax17)
false2claim6 = ProofItem("¬M(s,b,k)")
false2claim6.Requirements.Add(sax17)
false3claim6 = ProofItem("¬M(p,h,k)")
false3claim6.Requirements.Add(sax17)
false4claim6 = ProofItem("¬M(p,d,k)")
false4claim6.Requirements.Add(sax17)
false5claim6 = ProofItem("¬M(p,b,k)")
false5claim6.Requirements.Add(sax17)
false6claim6 = ProofItem("¬M(g,h,k)")
false6claim6.Requirements.Add(sax17)
false7claim6 = ProofItem("¬M(g,d,k)")
false7claim6.Requirements.Add(sax17)
false8claim6 = ProofItem("¬M(g,b,k)")
false8claim6.Requirements.Add(sax17)
false9claim6 = ProofItem("¬M(m,h,k)")
false9claim6.Requirements.Add(sax17)
false10claim6 = ProofItem("¬M(m,d,k)")
false10claim6.Requirements.Add(sax17)
false11claim6 = ProofItem("¬M(m,b,k)")
false11claim6.Requirements.Add(sax17)

sax17.OpensUp.Add(claim6)
sax17.OpensUp.Add(false1claim6)
sax17.OpensUp.Add(false2claim6)
sax17.OpensUp.Add(false3claim6)
sax17.OpensUp.Add(false4claim6)
sax17.OpensUp.Add(false5claim6)
sax17.OpensUp.Add(false6claim6)
sax17.OpensUp.Add(false7claim6)
sax17.OpensUp.Add(false8claim6)
sax17.OpensUp.Add(false9claim6)
sax17.OpensUp.Add(false10claim6)
sax17.OpensUp.Add(false11claim6)

#block 11
goal = ProofItem("M(s,h,c)")
goal.Requirements.Add(claim5)
goal.Requirements.Add(claim6)
goal.Requirements.Add(claim7)

falsegoal1 = ProofItem("M(p,h,r)")
falsegoal2 = ProofItem("M(g,h,c)")
falsegoal3 = ProofItem("M(m,h,r)")
falsegoal4 = ProofItem("M(s,h,r)")
falsegoal5 = ProofItem("M(p,h,c)")
falsegoal6 = ProofItem("M(g,h,r)")
falsegoal7 = ProofItem("M(m,h,c)")
falsegoal8 = ProofItem("M(m,d,c)")
falsegoal9 = ProofItem("M(p,h,k)")

goal.show()
falsegoal1.show()
falsegoal2.show()
falsegoal3.show()
falsegoal4.show()
falsegoal5.show()
falsegoal6.show()
falsegoal7.show()
falsegoal8.show()
falsegoal9.show()

