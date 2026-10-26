//Develop a Registration module using JSP, Servlet, and MVC architecture with database connectivity. 
//Collect user details like Username, Password, and Mobile. Store the data in a database upon form submission.

// user.java
package com.example;

public class User {

    private String username;
    private String password;
    private String mobile;

    public User() {
    }

    public User(String username, String password, String mobile) {
        this.username = username;
        this.password = password;
        this.mobile = mobile;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getMobile() {
        return mobile;
    }

    public void setMobile(String mobile) {
        this.mobile = mobile;
    }
}



// userDOA.java

package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class UserDAO {

    private String url = "jdbc:mysql://localhost:3306/j2ee_db";
    private String username = "root";
    private String password = "";

    public boolean registerUser(User user) {

        boolean status = false;

        try {
            // Load MySQL driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Create database connection
            Connection con = DriverManager.getConnection(
                    url, username, password);

            // SQL query
            String sql = "INSERT INTO `User` "
                       + "(username, password, mobile) "
                       + "VALUES (?, ?, ?)";

            PreparedStatement ps = con.prepareStatement(sql);

            ps.setString(1, user.getUsername());
            ps.setString(2, user.getPassword());
            ps.setString(3, user.getMobile());

            int result = ps.executeUpdate();

            if (result > 0) {
                status = true;
            }

            ps.close();
            con.close();

        } catch (Exception e) {
            e.printStackTrace();
        }

        return status;
    }
}


// registration_servlet.java

package com.example;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/register")
public class RegisterServlet extends HttpServlet {

    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response)
            throws ServletException, IOException {

        // Get data from registration form
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        String mobile = request.getParameter("mobile");

        // Create User object
        User user = new User(username, password, mobile);

        // Create DAO object
        UserDAO dao = new UserDAO();

        // Store user in database
        boolean status = dao.registerUser(user);

        if (status) {

            // Registration successful
            request.getRequestDispatcher("success.jsp")
                   .forward(request, response);

        } else {

            // Registration failed
            request.getRequestDispatcher("error.jsp")
                   .forward(request, response);
        }
    }
}




//register.jsp

<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
</head>
<body>

    <h2>User Registration</h2>

    <form action="register" method="post">

        <label>Username:</label>
        <input type="text" name="username" required>

        <br><br>

        <label>Password:</label>
        <input type="password" name="password" required>

        <br><br>

        <label>Mobile:</label>
        <input type="text" name="mobile" required>

        <br><br>

        <input type="submit" value="Register">

    </form>

</body>
</html>




// success.jsp

<!DOCTYPE html>
<html>
<head>
    <title>Registration Successful</title>
</head>
<body>

    <h2>Registration Successful!</h2>

    <p>Your details have been stored successfully in the database.</p>

    <a href="register.jsp">Register Another User</a>

</body>
</html>





// error.jsp

<!DOCTYPE html>
<html>
<head>
    <title>Registration Failed</title>
</head>
<body>

    <h2>Registration Failed</h2>

    <p>Unable to register the user.</p>

    <p>The username may already exist.</p>

    <a href="register.jsp">Try Again</a>

</body>
</html>




// 