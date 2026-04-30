from agents import BeslisRegelAgent, BasicAgent
from scenarios import get_basic_scenario
import model

scenario = get_basic_scenario()
agent = BasicAgent()

mod = model.Model(scenario,agent)

mod.run()
print(mod.move_log)
