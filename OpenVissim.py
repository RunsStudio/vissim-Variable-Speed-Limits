import win32com.client as com  # VISSIM COM
###########
## Author:  藏龙御景
## Date:    2020-01-22 
###########

class OpenVissim():  # 继承Problem父类
    def __init__(self, filename):
        self.incident = 0
        self.Vissim = com.Dispatch("Vissim.Vissim")
        dir = filename
        self.Vissim.LoadNet(dir)
        # Define Simulation Configurations
        graphics = self.Vissim.Graphics
        graphics.SetAttValue("VISUALIZATION", False)  ## 设为 不可见 提高效率
        self.Sim = self.Vissim.Simulation
        self.Net = self.Vissim.Net
        self.eval = self.Vissim.Evaluation
        print("载入路网完成！")
        self.decisions = self.Net.DesiredSpeedDecisions
        self.datacollections = self.Net.datacollections

    def runSimulation(self, accidentStartTime, accidentEndTime, totalPeriod, flagVSL):
        # # Set Simulation Parameters
        global vehicle4, vehicle3, vehicle2, vehicle1
        # Define total simulation period
        WarmPeriod = 900  # Define warm period 10 minutes
        Random_Seed = 42  # Define random seed
        step_time = 1  # Define Step Time
        self.Sim.Period = totalPeriod
        self.Sim.RandomSeed = 42
        # self.Sim.RunIndex= 1
        self.Sim.Resolution = step_time
        self.eval.SetAttValue("vehiclerecord", True)
        self.eval.SetAttValue("datacollection", True)

        for j in range(1, totalPeriod):
            if j == accidentStartTime:
                ###########
                ## Add Vehicle At Link Coordinate 参数：（车辆类型、期望速度、LINK编号、车道编号（最外侧为1）、里程坐标XCoord、交互模式 0）
                ###########
                vehicle1 = self.Net.vehicles.AddVehicleAtLinkCoordinate(100, 10, 4, 4, 750, 0)
                vehicle2 = self.Net.vehicles.AddVehicleAtLinkCoordinate(100, 10, 4, 3, 750, 0)
                vehicle3 = self.Net.vehicles.AddVehicleAtLinkCoordinate(100, 10, 4, 2, 750, 0)
                vehicle4 = self.Net.vehicles.AddVehicleAtLinkCoordinate(100, 10, 4, 1, 750, 0)
                vehicle1.SetAttValue("speed", 0)
                vehicle2.SetAttValue("speed", 0)
                vehicle3.SetAttValue("speed", 0)
                vehicle4.SetAttValue("speed", 0)
                self.incident = 1
                print("t=", j, "事故发生")
            if j == accidentEndTime:
                vehicle1.SetAttValue("speed", 80)
                vehicle2.SetAttValue("speed", 80)
                vehicle3.SetAttValue("speed", 80)
                vehicle4.SetAttValue("speed", 80)
                vehicle1.SetAttValue("DESIREDspeed", 80)
                vehicle2.SetAttValue("DESIREDspeed", 80)
                vehicle3.SetAttValue("DESIREDspeed", 80)
                vehicle4.SetAttValue("DESIREDspeed", 80)
                print("t=", j, "事故撤销")
            if j == accidentEndTime + 500:
                self.incident = 0
                print("t=", j, "VMS结束")
            if self.incident == 1 and j % 120 == 1 and flagVSL:
                for decision in self.decisions:
                    id = decision.ID
                    dataCollection = self.datacollections.GetDataCollectionByNumber(id)
                    spd = int(dataCollection.GetResult("speed", "mean", 0) / 10) * 10
                    # print(j, id, spd)
                    if spd == 110 or spd > 120:
                        spd = 120
                    if spd <= 60:
                        spd = 60
                    decision.SetAttValue("desiredspeed", spd)
            if self.incident == 0 and j % 120 == 1:
                for decision in self.decisions:
                    id = decision.ID
                    lane = id % 10
                    if lane == 1:
                        decision.SetAttValue("desiredspeed", 120)
                    if lane == 2 or lane == 3:
                        decision.SetAttValue("desiredspeed", 100)
                    if lane == 4:
                        decision.SetAttValue1("desiredspeed", 10, 90)
                        decision.SetAttValue1("desiredspeed", 20, 80)
            self.Sim.RunSingleStep()
        self.Sim.Stop()
        print("仿真结束")
