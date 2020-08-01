using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MongoDB.Driver;
using MongoDB.Bson;

namespace MongoApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var serverIP = "10.0.0.37";

            try
            {
                var dbClient = new MongoClient("mongodb://" + serverIP + ":27017");

                toolStripStatusLabel1.Text = "CONNECTED TO: " + serverIP;

                IMongoDatabase db = dbClient.GetDatabase("users");
                var data = db.GetCollection<BsonDocument>("users");
                var first = data.Find(new BsonDocument()).FirstOrDefault();
                var elements = new List<string>();

                foreach (var item in first)
                {
                    elements.Add(item.Value.ToString());

                }

                lblUserID.Text = elements[0];
                lbl_f_name.Text = elements[1];
                lbl_l_name.Text = elements[2];
            }
            catch 
            {
                toolStripStatusLabel1.Text = "ERROR CONNECTING TO: " + serverIP;
            }

        }
    }
}
