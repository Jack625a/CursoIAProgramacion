
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class CajeroAutomatico {
    private Map<String, Map<String, Integer>> usuarios;
    private String usuarioActual;

    public CajeroAutomatico() {
        usuarios = new HashMap<>();
        usuarios.put("usuario1", Map.of("contraseña", 1234, "saldo", 5200));
        usuarios.put("usuario2", Map.of("contraseña", 89562, "saldo", 10000));
        usuarioActual = null;
    }

    public boolean iniciarSesion(String usuario, String contraseña) {
        if (usuario.equals(usuarios.keySet().iterator().next()) && usuarios.get(usuario).get("contraseña").equals(Integer.parseInt(contraseña))) {
            usuarioActual = usuario;
            System.out.println("Bienvenido " + usuario);
            return true;
        } else {
            System.out.println("Usuario o contraseña incorrectos");
            return false;
        }
    }

    public void verSaldo() {
        if (usuarioActual != null) {
            System.out.println("El saldo de " + usuarioActual + " es " + usuarios.get(usuarioActual).get("saldo"));
        } else {
            System.out.println("No se ha iniciado sesion");
        }
    }

    public void depositar(int monto) {
        if (usuarioActual != null) {
            usuarios.get(usuarioActual).put("saldo", usuarios.get(usuarioActual).get("saldo") + monto);
            System.out.println("Se deposito " + monto + "Bs");
        } else {
            System.out.println("Debe iniciar sesion para continuar");
        }
    }

    public void retirar(int monto) {
        if (usuarioActual != null) {
            int saldoActual = usuarios.get(usuarioActual).get("saldo");
            if (monto <= saldoActual) {
                usuarios.get(usuarioActual).put("saldo", saldoActual - monto);
                System.out.println("Se retiró " + monto + "Bs");
            } else {
                System.out.println("Saldo insuficiente");
            }
        } else {
            System.out.println("Debe iniciar sesion para continuar");
        }
    }

    public void mostrarMenu() {
        while (true) {
            System.out.println("Menú principal:");
            System.out.println("1. Ver saldo");
            System.out.println("2. Depositar");
            System.out.println("3. Retirar");
            System.out.println("4. Salir");

            Scanner scanner = new Scanner(System.in);
            int opcion = scanner.nextInt();
            scanner.close();

            if (opcion == 1) {
                verSaldo();
            } else if (opcion == 2) {
                int monto = scanner.nextInt();
                depositar(monto);
            } else if (opcion == 3) {
                int monto = scanner.nextInt();
                retirar(monto);
            } else if (opcion == 4) {
                break;
            } else {
                System.out.println("Opción inválida. Por favor, seleccione una opción válida.");
            }
        }
    }

    public static void main(String[] args) {
        CajeroAutomatico cajero = new CajeroAutomatico();
        System.out.print("Ingrese su nombre de usuario: ");
        String user = System.in.nextLine();
    }
        