import py4j.GatewayServer;
import weka.core.SerializationHelper;

public class GatewayServerApp {
    private SerializationHelper serializationHelper;

    public GatewayServerApp() {
        // Initialize the SerializationHelper
        try {
            serializationHelper = new SerializationHelper();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public SerializationHelper getSerializationHelper() {
        return serializationHelper;
    }

    public static void main(String[] args) {
        GatewayServer server = new GatewayServer(new GatewayServerApp());
        server.start();
        System.out.println("Gateway Server Started");
    }
}
