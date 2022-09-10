import numpy as np
import pandas as pd
from pandas import isnull
from datetime import datetime

def map_row(row, tablename):
    # Preparar el renglon para insertarlo en la base de datos obras_procesado
    new_row = row
    if tablename == "datos_robot":
        return dict(index=new_row.index,timestamp=new_row.timestamp, actual_TCP_pose_0=new_row.actual_TCP_pose_0, actual_TCP_pose_1=new_row.actual_TCP_pose_1, actual_TCP_pose_2=new_row.actual_TCP_pose_2,
        actual_TCP_pose_3=new_row.actual_TCP_pose_3, actual_TCP_pose_4=new_row.actual_TCP_pose_4, actual_TCP_pose_5=new_row.actual_TCP_pose_5, actual_digital_input_bits=new_row.actual_digital_input_bits, joint_temperatures_0=new_row.joint_temperatures_0,
         joint_temperatures_1=new_row.joint_temperatures_1, joint_temperatures_2=new_row.joint_temperatures_2, joint_temperatures_3=new_row.joint_temperatures_3, joint_temperatures_4=new_row.joint_temperatures_4, joint_temperatures_5=new_row.joint_temperatures_5, actual_robot_voltage=new_row.actual_robot_voltage, actual_robot_current=new_row.actual_robot_current, 
         actual_joint_voltage_0=new_row.actual_joint_voltage_0, actual_joint_voltage_1=new_row.actual_joint_voltage_1, actual_joint_voltage_2=new_row.actual_joint_voltage_2, actual_joint_voltage_3=new_row.actual_joint_voltage_3, actual_joint_voltage_4=new_row.actual_joint_voltage_4, actual_joint_voltage_5=new_row.actual_joint_voltage_5, tool_temperature=new_row.tool_temperature)


def prepare_for_insertion(df, tablename):
    to_insert = list()
    for row in df.itertuples():
        to_insert.append(map_row(row, tablename))
    return to_insert