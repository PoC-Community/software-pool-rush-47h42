import express, { Request, Response } from 'express';
import { createUser, getUser } from 'API/user';
import jwt from 'jsonwebtoken';
import env_var from 'env-var';
import dotenv from 'dotenv'
import { StatusCodes, ReasonPhrases } from 'http-status-codes';
import bcrypt from 'bcryptjs';

dotenv.config();

const app = express();

function check_email(email: string): boolean {
    let reg = new RegExp('([a-z0-9]\w+\.[a-z0-9]\w+(@epitech.eu))');
    if (reg.test(email) === false)
        return false
    if (getUser(email) == null)
        return true
    return false
}

app.post('/register', (req: Request, res: Response) => {
    let email: string = req.body.email;
    let password: string = req.body.password;

    if (email === undefined || check_email(email) === false || password === undefined) {
        res.status(StatusCodes.BAD_REQUEST).send(ReasonPhrases.BAD_REQUEST);
    }
    let hashPassword = bcrypt.hashSync(password);
    const user = createUser(email, hashPassword);
    const token = jwt.sign(user, process.env.SECRET!, {expiresIn: '1day'});
    res.status(StatusCodes.CREATED).send(ReasonPhrases.CREATED);
});

app.post('/login', (req: Request, res: Response) => {
    let email: string = req.body.email;
    let password: string = req.body.password;

    if (email === undefined || password === undefined) {
        res.status(StatusCodes.BAD_REQUEST).send(ReasonPhrases.BAD_REQUEST);
    }
});
