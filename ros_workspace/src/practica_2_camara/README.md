# practica_2_camara

## Lanzador inicial de la cámara

El lanzador inicia el nodo `usb_cam` con una ruta de cámara configurable. Por defecto utiliza `/dev/video0` dentro del contenedor. La cámara debe estar conectada y ser accesible desde el contenedor.

En una terminal del contenedor, compila el paquete y carga el entorno:

```bash
cd ~/ros_workspace
colcon build --symlink-install --packages-select practica_2_camara
source install/setup.bash
```

Arranca el publicador:

```bash
ros2 launch practica_2_camara camara.launch.py
```

Si el dispositivo tiene otra ruta, por ejemplo `/dev/video2`:

```bash
ros2 launch practica_2_camara camara.launch.py video_device:=/dev/video2
```

En otra terminal del contenedor, comprueba los topics publicados con `ros2 topic list`. La imagen se espera en `/camera/image_raw`; la prueba con una cámara real aún está pendiente.
