from CCTutorEngine import *

ProblemDescription.Text = "Emily and Catherine each have their own pizza. Using the given assumptions, prove that Emily is not lactose intolerant."

goal = ProofItem("Emily is not lactose intolerant.")
goal.show()

axiom1 = ProofItem("Any pizza that has pepperoni also has cheese.")
axiom1.isAssumption = True
axiom1.show()

axiom2 = ProofItem("Either Catherine's pizza or Emily's pizza, or both, has pepperoni, but Catherine's pizza does not have cheese.")
axiom2.isAssumption = True
axiom2.show()

axiom3 = ProofItem("If someone is lactose intolerant, then their pizza does not have cheese.")
axiom3.isAssumption = True
axiom3.show()

ass1 = ProofItem("If Catherine's pizza has pepperoni, then Catherine's pizza also has cheese.")
ass1.Requirements.Add(axiom1)
ass1.show()

ass1b = ProofItem("If Catherine's pizza does not have cheese, then Catherine's pizza does not have pepperoni.")
ass1b.Requirements.Add(ass1)
ass1b.show()

ass2 = ProofItem("If Emily's pizza has pepperoni, then Emily's pizza also has cheese.")
ass2.Requirements.Add(axiom1)
ass2.show()

ass3 = ProofItem("Catherine's pizza does not have cheese.")
ass3.Requirements.Add(axiom2)
ass3.show()

bass3 = ProofItem("Catherine is lactose intolerant.")
bass3.show()

bass3b = ProofItem("Catherine's pizza has cheese.")
bass3b.show()

ass4 = ProofItem("Either Catherine's pizza or Emily's pizza, or both, has pepperoni.")
ass4.Requirements.Add(axiom2)
ass4.show()

ass5 = ProofItem("Catherine's pizza does not have pepperoni.")
ass5.Requirements.Add(ass1b)
ass5.Requirements.Add(ass3)
ass5.show()

bass5 = ProofItem("Catherine's pizza has pepperoni.")
bass5.show()

ass6 = ProofItem("Emily's pizza has pepperoni.")
ass6.Requirements.Add(ass4)
ass6.Requirements.Add(ass5)
ass6.show()

bass6 = ProofItem("Emily's pizza does not have pepperoni.")
bass6.show()

ass7 = ProofItem("Emily's pizza has cheese.")
ass7.Requirements.Add(ass6)
ass7.Requirements.Add(ass2)
ass7.show()

bass7 = ProofItem("Emily's pizza doe not have cheese.")
bass7.show()

ass8 = ProofItem("If someone's pizza has cheese, then they are not lactose intolerant.")
ass8.Requirements.Add(axiom3)
ass8.show()

bass8 = ProofItem("If someone's pizza does not have cheese, then they are lactose intolerant.")
bass8.show()

goal.Requirements.Add(ass8)
goal.Requirements.Add(ass7)

basscomplex = ProofItem("Catherine's pizza has pepperoni and cheese.")
basscomplex.Requirements.Add(bass3b)
basscomplex.Requirements.Add(bass5)
basscomplex.show()
