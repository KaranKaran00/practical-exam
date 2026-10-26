//Write a program that performs CRUD operation on product table having fields like pid,productname, price and quatity.

// index. html
<!DOCTYPE html>
<html>

<head>
    <title>Product CRUD</title>
</head>

<body>

    <h2>Product CRUD Operation</h2>

    <h3>Insert Product</h3>

    <form action="productCRUD" method="post">

        <input type="hidden" name="action" value="insert">

        Product ID:
        <input type="number" name="pid" required>

        <br><br>

        Product Name:
        <input type="text" name="productname" required>

        <br><br>

        Price:
        <input type="number" step="0.01" name="price" required>

        <br><br>

        Quantity:
        <input type="number" name="quantity" required>

        <br><br>

        <input type="submit" value="Insert Product">

    </form>

    <hr>

    <h3>Display Products</h3>

    <form action="productCRUD" method="get">

        <input type="submit" value="Display All Products">

    </form>

    <hr>

    <h3>Update Product</h3>

    <form action="productCRUD" method="post">

        <input type="hidden" name="action" value="update">

        Product ID:
        <input type="number" name="pid" required>

        <br><br>

        New Product Name:
        <input type="text" name="productname" required>

        <br><br>

        New Price:
        <input type="number" step="0.01" name="price" required>

        <br><br>

        New Quantity:
        <input type="number" name="quantity" required>

        <br><br>

        <input type="submit" value="Update Product">

    </form>

    <hr>

    <h3>Delete Product</h3>

    <form action="productCRUD" method="post">

        <input type="hidden" name="action" value="delete">

        Product ID:
        <input type="number" name="pid" required>

        <br><br>

        <input type="submit" value="Delete Product">

    </form>

</body>

</html>



// create servlet- productcrudservlet.java

package com.example;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/productCRUD")
public class ProductCRUDServlet extends HttpServlet {

    String url = "jdbc:mysql://localhost:3306/j2ee_db";
    String username = "root";
    String password = "";

    // CREATE, UPDATE and DELETE
    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");

        PrintWriter out = response.getWriter();

        String action = request.getParameter("action");

        try {

            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    url, username, password);

            // CREATE / INSERT
            if (action.equals("insert")) {

                int pid = Integer.parseInt(
                        request.getParameter("pid"));

                String productname =
                        request.getParameter("productname");

                double price = Double.parseDouble(
                        request.getParameter("price"));

                int quantity = Integer.parseInt(
                        request.getParameter("quantity"));

                String sql = "INSERT INTO product "
                        + "(pid, productname, price, quantity) "
                        + "VALUES (?, ?, ?, ?)";

                PreparedStatement ps =
                        con.prepareStatement(sql);

                ps.setInt(1, pid);
                ps.setString(2, productname);
                ps.setDouble(3, price);
                ps.setInt(4, quantity);

                int result = ps.executeUpdate();

                if (result > 0) {
                    out.println("<h2>Product Inserted Successfully!</h2>");
                }

                ps.close();
            }

            // UPDATE
            else if (action.equals("update")) {

                int pid = Integer.parseInt(
                        request.getParameter("pid"));

                String productname =
                        request.getParameter("productname");

                double price = Double.parseDouble(
                        request.getParameter("price"));

                int quantity = Integer.parseInt(
                        request.getParameter("quantity"));

                String sql = "UPDATE product SET "
                        + "productname = ?, price = ?, quantity = ? "
                        + "WHERE pid = ?";

                PreparedStatement ps =
                        con.prepareStatement(sql);

                ps.setString(1, productname);
                ps.setDouble(2, price);
                ps.setInt(3, quantity);
                ps.setInt(4, pid);

                int result = ps.executeUpdate();

                if (result > 0) {
                    out.println("<h2>Product Updated Successfully!</h2>");
                } else {
                    out.println("<h2>Product Not Found!</h2>");
                }

                ps.close();
            }

            // DELETE
            else if (action.equals("delete")) {

                int pid = Integer.parseInt(
                        request.getParameter("pid"));

                String sql =
                        "DELETE FROM product WHERE pid = ?";

                PreparedStatement ps =
                        con.prepareStatement(sql);

                ps.setInt(1, pid);

                int result = ps.executeUpdate();

                if (result > 0) {
                    out.println("<h2>Product Deleted Successfully!</h2>");
                } else {
                    out.println("<h2>Product Not Found!</h2>");
                }

                ps.close();
            }

            con.close();

            out.println("<br>");
            out.println("<a href='index.html'>Go Back</a>");

        } catch (Exception e) {

            out.println("<h3>Error: " + e.getMessage() + "</h3>");
        }
    }


    // READ / DISPLAY
    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");

        PrintWriter out = response.getWriter();

        try {

            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    url, username, password);

            String sql = "SELECT * FROM product";

            Statement stmt = con.createStatement();

            ResultSet rs = stmt.executeQuery(sql);

            out.println("<html>");
            out.println("<head>");
            out.println("<title>Product List</title>");
            out.println("</head>");

            out.println("<body>");

            out.println("<h2>All Product Records</h2>");

            out.println("<table border='1' cellpadding='10'>");

            out.println("<tr>");
            out.println("<th>Product ID</th>");
            out.println("<th>Product Name</th>");
            out.println("<th>Price</th>");
            out.println("<th>Quantity</th>");
            out.println("</tr>");

            while (rs.next()) {

                out.println("<tr>");

                out.println("<td>"
                        + rs.getInt("pid")
                        + "</td>");

                out.println("<td>"
                        + rs.getString("productname")
                        + "</td>");

                out.println("<td>"
                        + rs.getDouble("price")
                        + "</td>");

                out.println("<td>"
                        + rs.getInt("quantity")
                        + "</td>");

                out.println("</tr>");
            }

            out.println("</table>");

            out.println("<br>");

            out.println("<a href='index.html'>Go Back</a>");

            out.println("</body>");
            out.println("</html>");

            rs.close();
            stmt.close();
            con.close();

        } catch (Exception e) {

            out.println("<h3>Error: " + e.getMessage() + "</h3>");
        }
    }
}