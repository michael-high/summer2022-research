import random

class data():
    examples = []

    def add(self,ex):
        self.examples.append(ex)
    
    def total(self):
        return len(self.examples)
    
    def __init__(self):
        self.examples = []

    def makeSingleExp(self,num = 1):
        assert num + 1 <= self.total(), f"Maximum possible in context examples {self.total() -1}, got {num}"
        ex = self.examples.copy()
        random.shuffle(ex)
        p = ex.pop()
        experiment = ""
        for _ in range(num):
            a = ex.pop()
            for ass in a.getAssumptions():
                experiment += ass
            experiment += a.getProof() + "###\n"
        for ass in p.getAssumptions():
            experiment += ass
        experiment += "Proof:"
        return experi(exp= experiment, proof = p.getProof())

    def makeTrials(self,num = 1,trials = 1):
        assert num + 1 <= self.total(), f"Maximum possible in context examples {self.total() -1}, got {num}"
        ex = self.examples.copy()
        experiments = []
        random.shuffle(ex)
        p = ex.pop()
        for _ in range(trials):
            experiment = ""
            exa = ex.copy()
            random.shuffle(exa)
            for _ in range(num):
                a = exa.pop()
                for ass in a.getAssumptions():
                    experiment+= ass
                experiment += a.getProof() + "###\n"
            for ass in p.getAssumptions():
                experiment += ass
            experiment += "Proof:"
            experiments.append(experi(exp = experiment,proof = p.getProof()))

        return experiments


        

    def makeAllExps(self,num = 1):
        assert num + 1 <= self.total(), f"Maximum possible in context examples {self.total() -1}, got {num}"
        experiments = []
        for exa in self.examples:
            experiment = ""
            ex = self.examples.copy()
            ex.remove(exa)
            random.shuffle(ex)
            for _ in range(num):
                a = ex.pop()
                for ass in a.getAssumptions():
                    experiment += ass
                experiment += a.getProof() + "###\n"
            for ass in exa.getAssumptions():
                experiment += ass
            experiment += "Proof:"
            experiments.append(experi(exp = experiment,proof = exa.getProof()))
        return experiments

    def makeMultiExps(self,num = 1):
        assert num + 1 <= self.total(), f"Maximum possible in context examples {self.total() -1}, got {num}"
        experiments = []
        for exa in self.examples:
            experiment = ""
            ex = self.examples.copy()
            ex.remove(exa)
            random.shuffle(ex)
            for _ in range(num):
                a = ex.pop()
                for ass in a.getAssumptions():
                    experiment += ass
                experiment += a.getProofstr() + "###\n"
            for ass in exa.getAssumptions():
                experiment += ass
            
            experiments.append(experi(exp = experiment,proof = exa.getProofstr()))
        return experiments

class example():
    assumptions = []
    proof = ""

    def __init__(self):
        self.assumptions = []
        self.proof = ""

    def addAssumption(self,assumption):
        self.assumptions.append(assumption)

    def addProof(self,proof):
        self.proof = proof

    def getProof(self):
        return self.proof
    
    def getAssumptions(self):
        return self.assumptions

    def __str__(self):
        return str(self.assumptions) + " " + self.proof

class multiExp():
    assumptions = []
    proofs = {}
    proofstr = ""

    def __init__(self) -> None:
        self.assumptions = []
        self.proofs = {}
        self.proofstr = ""

    def addAssumption(self,assumption):
        self.assumptions.append(assumption)
    
    def addProof(self,a,b):
        self.proofs[a] = b
    
    def addProofstr(self,a):
        self.proofstr = self.proofstr + a
    
    def getProofstr(self):
        return self.proofstr

    def getAssumptions(self):
        return self.assumptions
    


class experi():
    exp = ""
    troof = ""
    def __init__(self,exp,proof):
        self.exp = exp
        if "Proof" in proof:
            self.troof = proof.split("Proof: ")[1]
        else:
            self.troof = proof
    def getExp(self):
        return self.exp
    def getTroof(self):
        return self.troof

