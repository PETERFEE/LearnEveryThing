# Capstone Blueprints: Proof of Embedded / Robotics Engineering Skill

## Blueprint A — Robust MCU Wireless Gateway

**Typical hardware:** any Cortex-M MCU with UART/DMA + an ESP32 or similar networking MCU; sensor or simulated inputs. Adapt to equipment already owned.

**Architecture:** Sensor/encoder → timer/ISR + DMA → RTOS message/queue → framed UART with CRC + timeout → wireless BLE/Wi-Fi/MQTT → PC test harness.

**Build steps:** bring up sensor and timestamping; implement state-machine driver; separate driver/service/application layers; define framing and version; implement producer/consumer; write host-side tests; record power and timing where meters are available.

**Safety:** watchdog, bounded buffers, invalid-packet rejection, loss-of-command safe state, power-on safe state; when motors are involved test unloaded, with a physically independent stop.

**Measures to collect, not fabricate:** timestamp jitter/percentiles, packet corruption/drop rate, recover-to-ready time, task stack headroom, memory footprint, throughput, and power current if measured with suitable equipment.

## Blueprint B — Linux / ROS 2 ↔ MCU Differential Drive

**Architecture:** Nav2 → `ros2_control` hardware plugin → serial/CAN protocol → MCU RTOS PID + encoder → motor; RPLIDAR → ROS 2 scans → SLAM Toolbox → TF2/odom → Nav2.

**Build steps:** begin in supported Gazebo; create a reproducible frame tree; implement differential drive kinematics; define MCU command/telemetry protocol and watchdog; integrate `ros2_control`; record rosbag; add launch tests; run repeated navigation trials.

**Safety:** software watchdog and hardware emergency stop. Fail motor actuation closed on stale or malformed commands. Prefer indoor, low-speed, low-load bench tests.

**Measures to collect:** command latency distribution, control jitter, missed deadlines, wheel velocity tracking, odometry drift, TF timestamp errors, navigation success fraction with stated sample count and failure modes.

## Blueprint C — Linux to MCU Systems Benchmark

Implement a like-for-like gateway via POSIX C++ serial, ROS 2 rclcpp and optionally micro-ROS. Hold traffic and hardware steady. Compare latency distributions, CPU/RAM, recovery, code complexity, and test reproducibility. Do not conclude one stack is faster without actual measurements.

## Portfolio expectations

Repository must show hardware diagram, interface contract, pinned SDK/ROS versions, `README.md` quickstart, `docs/architecture.md`, build commands, tests/CI where feasible, safety notes, logs/CSV, plots, and one bug postmortem. Describe **your own** specific contributions. Provide multilingual summaries only where useful to the learner's applications.
