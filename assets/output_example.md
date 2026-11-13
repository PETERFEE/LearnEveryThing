# Example output (fictional learner)

**Target:** Entry-level MCU firmware or ROS 2 software. **Inputs:** C/C++ and STM32 basics; Linux PC; 8 h/week; seeks stronger RTOS and robotics testing.

## Gaps

1. RTOS scheduling, ISR handoff, race/fault handling.
2. ROS 2 C++ nodes and coordinate frames.
3. Firmware unit tests and testable interfaces.
4. Linux process, serial, and cross-compilation workflows.

## Shortlist (illustrative)

- A01 Miro Samek / Quantum Leaps — firmware machine model.
- B01 FreeRTOS kernel book — scheduling, task notifications, timing.
- C05 CMake tutorial — reproducible builds.
- C07 Unity tests — host-side firmware logic verification.
- D01 ROS 2 official tutorials — rclcpp, launch, services and actions.
- D06 ros2_control — ROS ↔ actuator integration.

## Week 1

Read selected A01 sections, build a register/interrupt experiment, record timing with a logic analyzer or virtual test harness. **Exit criterion:** demonstrate and explain one timed MCU event plus a reproducible build.

**Caveat:** Current distro/support and URLs must be checked before a learner follows an old version-specific procedure.
