// Write a Contact Management System using MVC where users can add contacts with names and phone numbers, 
// and view all saved contacts. The Model handles contact data and interactions with the data store, 
// the View includes a form for adding contacts and a display page for listing them, and the Controller processes input from the form, 
// updates the model, and directs users to the appropriate view.

// contact.java 
package com.example;

public class Contact {

    private String name;
    private String phone;

    public Contact() {
    }

    public Contact(String name, String phone) {
        this.name = name;
        this.phone = phone;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
}




// contactDOA.java

package com.example;

import java.util.ArrayList;
import java.util.List;

public class ContactDAO {

    // Data store
    private static List<Contact> contacts = new ArrayList<Contact>();

    // Add contact
    public void addContact(Contact contact) {
        contacts.add(contact);
    }

    // Get all contacts
    public List<Contact> getAllContacts() {
        return contacts;
    }
}




// connectservlet.java

package com.example;

import java.io.IOException;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/contacts")
public class ContactServlet extends HttpServlet {

    private ContactDAO contactDAO = new ContactDAO();

    protected void doPost(HttpServletRequest request,
                          HttpServletResponse response)
            throws ServletException, IOException {

        // Get data from form
        String name = request.getParameter("name");
        String phone = request.getParameter("phone");

        // Create Contact object
        Contact contact = new Contact(name, phone);

        // Add contact to model
        contactDAO.addContact(contact);

        // Redirect to display page
        response.sendRedirect("contacts");
    }

    protected void doGet(HttpServletRequest request,
                         HttpServletResponse response)
            throws ServletException, IOException {

        // Get all contacts from model
        List<Contact> contacts = contactDAO.getAllContacts();

        // Store contacts in request
        request.setAttribute("contacts", contacts);

        // Forward to JSP
        request.getRequestDispatcher("contacts.jsp")
               .forward(request, response);
    }
}






// index.jsp

<!DOCTYPE html>
<html>
<head>
    <title>Contact Management System</title>
</head>
<body>

    <h2>Contact Management System</h2>

    <h3>Add New Contact</h3>

    <form action="contacts" method="post">

        <label>Name:</label>
        <input type="text" name="name" required>

        <br><br>

        <label>Phone Number:</label>
        <input type="text" name="phone" required>

        <br><br>

        <input type="submit" value="Add Contact">

    </form>

    <br>

    <a href="contacts">View All Contacts</a>

</body>
</html>





// contacts.jsp

<%@ page import="java.util.List" %>
<%@ page import="com.example.Contact" %>

<!DOCTYPE html>
<html>
<head>
    <title>All Contacts</title>
</head>
<body>

    <h2>All Saved Contacts</h2>

    <%
        List<Contact> contacts =
            (List<Contact>) request.getAttribute("contacts");

        if (contacts != null && !contacts.isEmpty()) {
    %>

        <table border="1" cellpadding="10">

            <tr>
                <th>No.</th>
                <th>Name</th>
                <th>Phone Number</th>
            </tr>

            <%
                int count = 1;

                for (Contact contact : contacts) {
            %>

            <tr>
                <td><%= count++ %></td>
                <td><%= contact.getName() %></td>
                <td><%= contact.getPhone() %></td>
            </tr>

            <%
                }
            %>

        </table>

    <%
        } else {
    %>

        <p>No contacts available.</p>

    <%
        }
    %>

    <br>

    <a href="index.jsp">Add New Contact</a>

</body>
</html>