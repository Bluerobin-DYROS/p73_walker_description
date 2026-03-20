import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path("p73_walker.urdf")
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data):
    while True:
        mujoco.mj_step(model, data)