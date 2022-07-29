from src.ds import example, data
from src.utils import parse, parseMulti, removeCause
from src.runner import runner
from src.upload import uploader



def main(filename):
    a = parse(f"C:\CS\SUM2022\SUM2022-github\Jurassic\\fine-tuning\inferences\\{filename}.txt")
    #a = parseMulti("./data/multi")
    experiments =a.makeAllExps(30)
    #experiments =a.makeTrials(10,5)
    #experiments = a.makeMultiExps(40)

    u=uploader(experiments=experiments)
    u.convert()

    # r = runner(path=f"C:\CS\SUM2022\SUM2022-github\Jurassic\\fine-tuning\generation\generated\{filename}.txt",openAIKey="")
    # r.setAI21Key("Bearer ")
    # r.add(experiments)


    # r.run(provider="AI21",model="j1-jumbo")
    #r.rumMulti()
    #r.runModels()
    #r.runTrials()




    #removeCause("./data/test")




if __name__ == "__main__":
    main("tollens")
