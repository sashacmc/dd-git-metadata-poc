import ddtrace

from ddtrace.profiling import Profiler

prof = Profiler()
prof.start()

def send_span():
    with ddtrace.tracer.trace("gitmetadata.test.span"):
        raise Exception("some error")


if __name__ == "__main__":
    send_span()
