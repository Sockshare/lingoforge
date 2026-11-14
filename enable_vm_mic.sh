#!/usr/bin/env bash
# Automatically links the active Chrome Remote Desktop PipeWire/PulseAudio microphone
# socket into /run/user/$UID/pulse/native and /run/user/$UID/pipewire-0 so browsers inside
# the VM can directly access the user's physical hardware microphone via CRD Audio Input!
UID_DIR="/run/user/$(id -u)"
CRD_DIR=$(ls -td "$UID_DIR"/crd_audio* 2>/dev/null | head -n 1)
if [ -n "$CRD_DIR" ]; then
  mkdir -p "$UID_DIR/pulse"
  ln -sf "$CRD_DIR/native" "$UID_DIR/pulse/native"
  ln -sf "$CRD_DIR/pipewire" "$UID_DIR/pipewire-0"
  echo "[LingoForge Audio] Linked VM default microphone to: $CRD_DIR (Chrome Remote Desktop Audio Input)"
fi
