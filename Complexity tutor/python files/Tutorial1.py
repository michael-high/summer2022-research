from CCTutorEngine import *

ProblemDescription.Text = "Mark is a good computer scientist. Working with the assumptions below, prove that he knows algorithms."

goal = ProofItem("Mark knows algorithms")
goal.show()
               
axiom0 = ProofItem("Mark is a good computer scientist.")
axiom0.isAssumption = True
axiom0.show()

axiom1 = ProofItem("All good computer scientists have a degree in computer science.")
axiom1.isAssumption = True
axiom1.show()

axiom2 = ProofItem("If you have a degree in X then you passed all required classes for the X major.")
axiom2.isAssumption = True
axiom2.show()

axiom3 = ProofItem("If you passed a class in X then you know X.")
axiom3.isAssumption = True
axiom3.show()

axiom4 = ProofItem("Algorithms is a required class for the computer science major.")
axiom4.isAssumption = True
axiom4.show()

axiom5 = ProofItem("If someone knows algorithsm, then they are a good computer scientist.")
axiom5.isAssumption = True
axiom5.show()

state1 = ProofItem("Mark has a degree in computer science.")
state1.Requirements.Add(axiom0)
state1.Requirements.Add(axiom1)

state2b = ProofItem("Mark passed all required classes for the computer science major.")
state2b.Requirements.Add(state1)
state2b.Requirements.Add(axiom2)

state2 = ProofItem("Mark passed an algorithms class.")
state2.Requirements.Add(state2b)
state2.Requirements.Add(axiom4)

badone = ProofItem("Mark passed out while studying algorithms.")
badone.isWrong = True

goal.Requirements.Add(axiom3)
goal.Requirements.Add(state2)

axiom0.OpensUp.Add(state1)
state1.OpensUp.Add(state2)
state1.OpensUp.Add(state2b)
state1.OpensUp.Add(badone)
