from CCTutorEngine import *

ProblemDescription.Text = "Suppose there are 3 dogs -- Biscuit, Cardie and Duncan. Prove that Duncan is not muddy."

goal = ProofItem("Duncan is not muddy")
goal.show()

asm1 = ProofItem("Either Cardie or Biscuit, but not both, went in the pond, and if Cardie is not muddy then Biscuit is muddy")
asm1.isAssumption = True
asm1.show()

asm2 = ProofItem("A dog is wet if and only if it went in the pond or it went in the swamp")
asm2.isAssumption = True
asm2.show()

asm3 = ProofItem("Every muddy dog went in the swamp, and every dog who went in the pond is not muddy")
asm3.isAssumption = True
asm3.show()

asm4 = ProofItem("Not all of the three dogs are wet")
asm4.isAssumption = True
asm4.show()

proof1 = ProofItem("Duncan did not go in the swamp")
goal.Requirements.Add(proof1)

proof2 = ProofItem("Every dog that did not go in the swamp is not muddy")
goal.Requirements.Add(proof2)

proof2.Requirements.Add(asm3)

proof3 = ProofItem("Duncan is not wet")
proof3.show()
proof1.Requirements.Add(proof3)

proof4 = ProofItem("Dogs that are not wet did not go in the pond or swamp")
proof1.Requirements.Add(proof4)

proof4.Requirements.Add(asm2)

proof5 = ProofItem("At least one of the three dogs, Duncan, Cardie or Biscuit, is not wet")
proof5.Requirements.Add(asm4)

proof6 = ProofItem("If Biscuit is muddy, then Cardie is not muddy")
proof6.show()
proof6.isWrong = True

proof7 = ProofItem("If Biscuit is not muddy, then Cardie is muddy")
proof7.show()
proof7.Requirements.Add(asm1)

proof8 = ProofItem("If Cardie went in the pond, then Cardie is not muddy")
proof8.show()
proof8.Requirements.Add(asm3)

proof9 = ProofItem("If Cardie went in the pond, then Cardie is wet")
proof9.show()
proof9.Requirements.Add(asm2)

proof10 = ProofItem("If Cardie went in the swamp, then Cardie is muddy")
proof10.show()
proof10.isWrong = True

proof11 = ProofItem("If Cardie went in the swamp, then Cardie is wet")
proof11.show()
proof11.Requirements.Add(asm2)

proof12 = ProofItem("If Cardie went in the pond, then Biscuit is muddy")
proof12.Requirements.Add(proof8)
proof12.Requirements.Add(asm1)
asm1.OpensUp.Add(proof12)

proof13 = ProofItem("If Cardie went in the pond, then Biscuit went in the swamp")
proof13.Requirements.Add(proof12)
proof13.Requirements.Add(asm3)
proof12.OpensUp.Add(proof13)

proof14 = ProofItem("If Cardie went in the pond, then Biscuit is wet")
proof14.Requirements.Add(proof13)
proof14.Requirements.Add(asm2)
proof13.OpensUp.Add(proof14)

proof15 = ProofItem("If Cardie went in the pond, then Cardie and Biscuit are wet")
proof15.Requirements.Add(proof14)
proof15.Requirements.Add(proof9)
proof14.OpensUp.Add(proof15)

proof8b = ProofItem("If Biscuit went in the pond, then Biscuit is not muddy")
proof8b.show()
proof8b.Requirements.Add(asm3)

proof9b = ProofItem("If Biscuit went in the pond, then Biscuit is wet")
proof9b.show()
proof9b.Requirements.Add(asm2)

proof10b = ProofItem("If Biscuit went in the swamp, then Biscuit is muddy")
proof10b.show()
proof10b.isWrong = True

proof11b = ProofItem("If Biscuit went in the swamp, then Biscuit is wet")
proof11b.show()
proof11b.Requirements.Add(asm2)

proof12b = ProofItem("If Biscuit went in the pond, then Cardie is muddy")
proof12b.Requirements.Add(proof8b)
proof12b.Requirements.Add(proof7)
proof7.OpensUp.Add(proof12b)

proof13b = ProofItem("If Biscuit went in the pond, then Cardie went in the swamp")
proof13b.Requirements.Add(proof12b)
proof13b.Requirements.Add(asm3)
proof12b.OpensUp.Add(proof13b)

proof14b = ProofItem("If Biscuit went in the pond, then Cardie is wet")
proof14b.Requirements.Add(proof13b)
proof14b.Requirements.Add(asm2)
proof13b.OpensUp.Add(proof14b)

proof15b = ProofItem("If Biscuit went in the pond, then Cardie and Biscuit are wet")
proof15b.Requirements.Add(proof14b)
proof15b.Requirements.Add(proof9b)
proof14b.OpensUp.Add(proof15b)

proof8d = ProofItem("If Duncan went in the pond, then Duncan is not muddy")
proof8d.show()
proof8d.Requirements.Add(asm3)

proof9d = ProofItem("If Duncan went in the pond, then Duncan is wet")
proof9d.show()
proof9d.Requirements.Add(asm2)

proof10d = ProofItem("If Duncan went in the swamp, then Duncan is muddy")
proof10d.show()
proof10d.isWrong = True

proof11d = ProofItem("If Duncan went in the swamp, then Duncan is wet")
proof11d.show()
proof11d.Requirements.Add(asm2)

proof16 = ProofItem("Cardie and Biscuit are wet")
proof16.show()
proof16.Requirements.Add(proof15)
proof16.Requirements.Add(proof15b)
proof16.Requirements.Add(asm1)

proof17 = ProofItem("Duncan and Biscuit are wet")
proof17.show()
proof17.isWrong = True

proof18 = ProofItem("Cardie and Biscuit are muddy")
proof18.show()
proof18.isWrong = True

proof19 = ProofItem("Cardie and Duncan are muddy")
proof19.show()
proof19.isWrong = True

proof20 = ProofItem("Cardie and Biscuit are not wet")
proof20.show()
proof20.isWrong = True

proof21 = ProofItem("Cardie and Duncan are not wet")
proof2.show()
proof21.isWrong = True

proof22 = ProofItem("Cardie or Duncan is wet")
proof22.show()
proof22.Requirements.Add(proof16)

proof23 = ProofItem("Cardie or Biscuit is not muddy")
proof23.show()
proof23.Requirements.Add(asm1)
proof23.Requirements.Add(proof8)
proof23.Requirements.Add(proof8b)

proof24 = ProofItem("Cardie or Biscuit is muddy")
proof24.show()
proof24.Requirements.Add(asm1)

proof25 = ProofItem("Duncan or Biscuit is wet")
proof25.show()
proof25.Requirements.Add(proof16)

proof26 = ProofItem("Biscuit is not wet")
proof26.show()
proof26.isWrong = True

proof3.Requirements.Add(proof16)
proof3.Requirements.Add(proof5)

proof27 = ProofItem("Duncan did not go in the pond")
proof27.Requirements.Add(proof3)
proof27.Requirements.Add(asm2)

proof28 = ProofItem("Every dog that is muddy did not go in the pond")
proof28.Requirements.Add(asm3)

proof29 = ProofItem("If Biscuit is muddy, then Biscuit did not go in the pond")
proof29.show()
proof29.Requirements.Add(proof28)

proof30 = ProofItem("If Cardie is muddy, then Cardie did not go in the pond")
proof30.show()
proof30.Requirements.Add(proof28)

proof31 = ProofItem("Cardie or Biscuit did not go in the pond")
proof31.Requirements.Add(proof28)
proof31.Requirements.Add(proof24)

proof32 = ProofItem("If Biscuit is not muddy, then Cardie did not go in the pond")
proof32.Requirements.Add(proof7)
proof32.Requirements.Add(proof28)

proof3.OpensUp.Add(proof1)
proof3.OpensUp.Add(proof27)
asm3.OpensUp.Add(proof2)
asm3.OpensUp.Add(proof28)
asm2.OpensUp.Add(proof4)
asm4.OpensUp.Add(proof5)
proof24.OpensUp.Add(proof31)
proof7.OpensUp.Add(proof32)
