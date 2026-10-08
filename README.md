# devops-revisao

## 23 - Repositório e commits
Perdi a log pois o pc reiniciou sozinho
## 24 - Branch feature-mensagem e merge
Perdi a log pois o pc reiniciou sozinho
## 25 - GitHub Actions
Perdi a log pois o pc reiniciou sozinho
## 26 - Porta e PID do http.server
TCP    0.0.0.0:8080           0.0.0.0:0              LISTENING       9280
  TCP    [::]:8080              [::]:0                 LISTENING       9280
  
  Nome da imagem            Identifi Nome da sessão       Sessão# Uso de memór
========================= ======== ================ =========== ============
python3.13.exe                9280 Console                    1     31.576 K

ÊXITO: o processo com PID 9280 foi finalizado.

## 28 - Docker build, run, ps e logs

[main b1b3169] build: adiciona Dockerfile
 2 files changed, 21 insertions(+)
 create mode 100644 .dockerignore
 create mode 100644 Dockerfile

 +] Building 19.4s (10/10) FINISHED                                                                                                       docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                      0.2s
 => => transferring dockerfile: 222B                                                                                                                      0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                                                                                       3.5s
 => [internal] load .dockerignore                                                                                                                         0.1s
 => => transferring context: 72B                                                                                                                          0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:05cda9777409a9c3ffddd94a4c476b79f0769a0b4857f0c7ed9226b6800b0d6f                                 5.1s
 => => resolve docker.io/library/python:3.12-slim@sha256:05cda9777409a9c3ffddd94a4c476b79f0769a0b4857f0c7ed9226b6800b0d6f                                 0.1s
 => => sha256:bbc5a12237474ec0b23b5051260d56d6436a24d70d9cad961adebe7a037ed813 249B / 249B                                                                0.2s
 => => sha256:6912e23eb44595b44dc6d9882b34f305ad6f6e9667cec70b13e5dbc4f8cd97f4 12.12MB / 12.12MB                                                          1.4s
 => => sha256:75b6a36c64a1cf3520fc4b4aae4739d5caa8a6a05c27835a920a61784c9c32f8 1.29MB / 1.29MB                                                            1.0s
 => => sha256:ecc510c1e359bdc007b39802570bb7e4dec7d6ebccf357c3201a74299113e05e 29.84MB / 29.84MB                                                          2.6s
 => => extracting sha256:ecc510c1e359bdc007b39802570bb7e4dec7d6ebccf357c3201a74299113e05e                                                                 1.0s
 => => extracting sha256:75b6a36c64a1cf3520fc4b4aae4739d5caa8a6a05c27835a920a61784c9c32f8                                                                 0.2s
 => => extracting sha256:6912e23eb44595b44dc6d9882b34f305ad6f6e9667cec70b13e5dbc4f8cd97f4                                                                 0.6s
 => => extracting sha256:bbc5a12237474ec0b23b5051260d56d6436a24d70d9cad961adebe7a037ed813                                                                 0.1s
 => [internal] load build context                                                                                                                         0.3s
 => => transferring context: 1.73kB                                                                                                                       0.0s
 => [2/5] WORKDIR /app                                                                                                                                    0.5s
 => [3/5] COPY requirements.txt .                                                                                                                         0.2s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                              4.1s
 => [5/5] COPY . .                                                                                                                                        0.2s
 => exporting to image                                                                                                                                    4.8s
 => => exporting layers                                                                                                                                   1.1s
 => => exporting manifest sha256:03c85237b1b0206ab63457ae876f9ba444f88506ef04bb9426d149c8e1087398                                                         0.1s
 => => exporting config sha256:6a717feab898fbc6af51cd859f3efc8a7e020d788db4702c5b30eb7498132db3                                                           0.1s
 => => exporting attestation manifest sha256:3bf5f39ab9f1719b34b125f635056d52c709a3144da1a3182d0776726a9becfe                                             0.1s
 => => exporting manifest list sha256:31ac93c98784067ddaad4044827685449db0ff5e0f6a20ea5017d41110ee4f63                                                    0.1s
 => => naming to docker.io/library/devops-revisao:latest                                                                                                  0.0s
 => => unpacking to docker.io/library/devops-revisao:latest

 326f5c1f2f25d43afaaefa3a894191d06749eeded61f63374f9c10a1ac981259

 CONTAINER ID   IMAGE            COMMAND           CREATED          STATUS          PORTS                                         NAMES
326f5c1f2f25   devops-revisao   "python app.py"   47 seconds ago   Up 46 seconds   0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp   devops-app

 Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [08/Oct/2026 04:55:44] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [08/Oct/2026 04:55:44] "GET /favicon.ico HTTP/1.1" 404 -