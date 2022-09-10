from DBHelper import db
from sqlalchemy import Column,Float


class datos_robot(db.Base):
    __tablename__ = "datos_robot"

    # Columnas
    index= Column(Float,primary_key=True)
    timestamp= Column(Float)
    actual_TCP_pose_0 = Column(Float)
    actual_TCP_pose_1 = Column(Float)
    actual_TCP_pose_2 = Column(Float)
    actual_TCP_pose_3 = Column(Float)
    actual_TCP_pose_4 = Column(Float)
    actual_TCP_pose_5 = Column(Float)
    actual_digital_input_bits =Column(Float)
    joint_temperatures_0 = Column(Float)
    joint_temperatures_1 = Column(Float)
    joint_temperatures_2 = Column(Float)
    joint_temperatures_3 = Column(Float)
    joint_temperatures_4 = Column(Float)
    joint_temperatures_5 = Column(Float)
    actual_robot_voltage = Column(Float)
    actual_robot_current = Column(Float)
    actual_joint_voltage_0 = Column(Float)
    actual_joint_voltage_1 = Column(Float)
    actual_joint_voltage_2 = Column(Float)
    actual_joint_voltage_3 = Column(Float)
    actual_joint_voltage_4 = Column(Float)
    actual_joint_voltage_5 = Column(Float)
    tool_temperature = Column(Float)

    def __init__(self, index, timestamp, actual_TCP_pose_0, actual_TCP_pose_1, actual_TCP_pose_2,
        actual_TCP_pose_3, actual_TCP_pose_4, actual_TCP_pose_5, actual_digital_input_bits, joint_temperatures_0,
         joint_temperatures_1, joint_temperatures_2, joint_temperatures_3, joint_temperatures_4, joint_temperatures_5, actual_robot_voltage, actual_robot_current, 
         actual_joint_voltage_0, actual_joint_voltage_1, actual_joint_voltage_2, actual_joint_voltage_3, actual_joint_voltage_4, actual_joint_voltage_5, tool_temperature):

        self.index = index
        self.timestamp = timestamp
        self.actual_TCP_pose_0 = actual_TCP_pose_0
        self.actual_TCP_pose_1 =actual_TCP_pose_1
        self.actual_TCP_pose_2 = actual_TCP_pose_2
        self.actual_TCP_pose_3 = actual_TCP_pose_3
        self.actual_TCP_pose_4 = actual_TCP_pose_4
        self.actual_TCP_pose_5 = actual_TCP_pose_5
        self.actual_digital_input_bits =actual_digital_input_bits
        self.joint_temperatures_0 = joint_temperatures_0
        self.joint_temperatures_1 = joint_temperatures_1
        self.joint_temperatures_2 = joint_temperatures_2
        self.joint_temperatures_3 = joint_temperatures_3
        self.joint_temperatures_4 = joint_temperatures_4
        self.joint_temperatures_5 = joint_temperatures_5
        self.actual_robot_voltage = actual_robot_voltage
        self.actual_robot_current = actual_robot_current
        self.actual_joint_voltage_0 = actual_joint_voltage_0
        self.actual_joint_voltage_1 = actual_joint_voltage_1
        self.actual_joint_voltage_2 = actual_joint_voltage_2
        self.actual_joint_voltage_3 = actual_joint_voltage_3
        self.actual_joint_voltage_4 = actual_joint_voltage_4
        self.actual_joint_voltage_5 = actual_joint_voltage_5
        self.tool_temperature = tool_temperature
        



