import { User } from '@prisma/client'
import prisma from './client'

export async function createUser(email: string, password: string): Promise<User> {
    const user = await prisma.user.create({
        data: {
            name: email,
            email: email,
            password: password,
            reports: {}
        }
    });
    return user;
}

export async function getUser(email: string): Promise<User | null> {
    const user = await prisma.user.findUnique({
        where: {
            email: email,
        },
    });
    return user;
}
