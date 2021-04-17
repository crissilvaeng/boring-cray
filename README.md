# Boring Cray

![Python v3.8](https://img.shields.io/badge/python-3.8-blue?style=for-the-badge)

## Proposal

> Nothing to see here, move along.

## Usage

Using VS Code with Dev Container, select `Open Folder in Container...` option.

### Running

- activities-service

```
root ➜ /workspace/activities-service (master) $ python api.py
 * Serving Flask app "config" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5003/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 331-766-217
```

- assessment-service

```
root ➜ /workspace/assessment-service (master ✗) $ python api.py  * Serving Flask app "config" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5004/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 331-766-217
```

- assessment-worker

```
root ➜ /workspace/assessment-worker (master) $ celery -A tasks worker --loglevel=INFO
/usr/local/lib/python3.8/site-packages/celery/platforms.py:796: RuntimeWarning: You're running the worker with superuser privileges: this is
absolutely not recommended!

Please specify a different user using the --uid option.

User information: uid=0 euid=0 gid=0 egid=0

  warnings.warn(RuntimeWarning(ROOT_DISCOURAGED.format(
 
 -------------- celery@668bdf83e57b v5.0.5 (singularity)
--- ***** ----- 
-- ******* ---- Linux-4.19.121-linuxkit-x86_64-with-glibc2.2.5 2021-04-17 01:02:46
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x7f05954727f0
- ** ---------- .> transport:   amqp://guest:**@broker:5672//
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 2 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . tasks.send_score_to_submission
  . tasks.send_submission_to_evaluation

[2021-04-17 01:02:46,888: INFO/MainProcess] Connected to amqp://guest:**@broker:5672//
[2021-04-17 01:02:46,923: INFO/MainProcess] mingle: searching for neighbors
[2021-04-17 01:02:48,279: INFO/MainProcess] mingle: all alone
[2021-04-17 01:02:48,315: INFO/MainProcess] celery@668bdf83e57b ready.
```

## License

The MIT License (MIT). To see the details of this license, see the [license file](LICENSE.md).

:octocat:
