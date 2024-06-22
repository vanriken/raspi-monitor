# Rapsberry Pi Monitor

A program to monitor your Raspberry Pi.

## Grafana
The idea is to forward the information to a Grafana dashboard. Then you can monitor the Raspberry Pi from there. To install Grafana on the Raspberry Pi, the steps on this [blog post](https://pimylifeup.com/raspberry-pi-grafana/). Once you have successfully installed Grafana, the service will be available at `http://<raspi-ip-address>:3000`.

## Poetry
This project uses Poetry for dependency management. 

If you install Poetry and the command is still not available, add `export PATH="$HOME/.local/bin:$PATH"` to `~/.bashrc`. To make Poetry install the virtual environments in the project directory, use the command `poetry config virtualenvs.in-project true`