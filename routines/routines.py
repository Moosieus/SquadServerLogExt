"""
Each of the classes below is a Routine
Every routine has each of the following:
    A title String
    An operation method
    A boolean, self.run
The
Routines must always accept the line as an argument, and return a string.

Every routine has a corresponding 'key', which can be found in the dataToLog dict.
Keys should not have spaces or the '$' character.
"""

from config.config import delimiter
from routines.routine import Routine

"""
ROUTINES
"""


class TimeStamp(Routine):
    title = "Time_Stamp"

    def operation(self, line):
        if line.startswith('[20'):
            return line[:20].strip('[]')
        return ''


class HardWare(Routine):
    title = "Hardware_Info"

    def __init__(self):
        super().__init__()
        self.data = {
            'OS': False,
            'VER': False,
            'CPU': False
        }

    def set_run(self, var):
        self.data[var] = True
        for value in self.data.values():
            if not value:
                self.run = True
                break
            else:
                self.run = False

    def operation(self, line):
        if not self.run:
            return ''
        else:
            if 'Selected Device Profile: ' in line and not self.data['OS']:
                self.set_run('OS')
                return line.split('Profile: ')[1].strip('\n')

            elif 'Initializing Squad version ' in line and not self.data['VER']:
                self.set_run('VER')
                return line.split(' Initializing Squad version ')[1].strip('\n')

            elif ' CPU Brand: ' in line and not self.data['CPU']:
                self.set_run('CPU')
                return line.split(' CPU Brand: ')[1].strip('\n')
            return ''


class TickRate(Routine):
    title = "Tick_Rate"

    def operation(self, line):
        if 'Server Tick Rate' in line:
            tick_rate = line.split('Server Tick Rate: ')[1]
            return tick_rate.strip('\n')
        return ''


class PlayerCount(Routine):
    title = "Player_Count"

    def operation(self, line):
        if 'PlayerCount_i:' in line:
            shouldLogZero = False  # Flip this to enable logging at zero.
            player_count = line.split('PlayerCount_i:')[1].split(' ')[0]
            if shouldLogZero:
                return player_count
            elif int(player_count) != 0:
                return player_count
        return ''


class MapName(Routine):
    title = "Map_Name"

    def operation(self, line):
        if 'StartNewGame(): ' in line:
            return line.split('/')[-1].strip('\n')
        return ''


"""
ROUTINES
"""


dataToLog = {
    TimeStamp.title: TimeStamp(),
    PlayerCount.title: PlayerCount(),
    TickRate.title: TickRate(),
    MapName.title: MapName(),
    HardWare.title: HardWare()
    }


def build_template_string():
    template = ''
    for key in dataToLog.keys():
        template += '$' + key + delimiter
    return template+'\n'
