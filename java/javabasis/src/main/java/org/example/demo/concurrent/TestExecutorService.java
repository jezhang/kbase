package org.example.demo.concurrent;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.*;

public class TestExecutorService {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        Map map = new HashMap();
        map.put("foo", "bar");
        Future<String> future = executor.submit(new Task(map));

        try {
            System.out.println("Started..");
            System.out.println(future.get(3, TimeUnit.SECONDS));
            System.out.println("Finished!");
        } catch (TimeoutException e) {
            future.cancel(true);
            System.out.println("Terminated!");
        }
        executor.shutdownNow();
    }
}


class Task implements Callable<String> {
    private Map params;

    public Map getParams() {
        return params;
    }

    public void setParams(Map params) {
        this.params = params;
    }

    public Task(Map params) {
        this.params = params;
    }

    @Override
    public String call() throws Exception {
        Thread.sleep(2000); // Just to demo a long running task of 4 seconds.
        System.out.println(params.get("foo"));
        return "Ready!";
    }
}
